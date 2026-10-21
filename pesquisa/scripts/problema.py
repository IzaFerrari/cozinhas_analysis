"""Gate 1B: a premissa de heterogeneidade sobrevive às tentativas de fazê-la desaparecer?

Lê o snapshot DATA1 (pesquisa/dados/brutos) e grava pesquisa/agregados/problema.csv.
Uso: python -I pesquisa/scripts/problema.py  (a partir da raiz do repositório)
"""
import re
import unicodedata
from pathlib import Path

import numpy as np
import pandas as pd

RAIZ = Path(__file__).resolve().parents[2]
BRUTOS = RAIZ / "pesquisa" / "dados" / "brutos"
SAIDA = RAIZ / "pesquisa" / "agregados" / "problema.csv"

contratacoes = pd.read_csv(BRUTOS / "contratacoes.csv", header=10)
unidades = pd.read_csv(BRUTOS / "unidades.csv", header=6)
juntos = contratacoes.merge(unidades, left_on="N° DO PROJETO", right_on="Num TPAF", how="left")


def normaliza(nome):
    # mesma normalização da exploração (explore3.py): sem acento, maiúsculas, sem preposições
    nome = unicodedata.normalize("NFKD", str(nome)).encode("ascii", "ignore").decode().upper()
    nome = re.sub(r"[^A-Z0-9 ]", " ", nome)
    nome = re.sub(r"\b(DA|DE|DO|DAS|DOS|E)\b", " ", nome)
    return re.sub(r"\s+", " ", nome).strip()


juntos["nome_norm"] = juntos["Nome Consumidor"].where(juntos["Nome Consumidor"].isna(), juntos["Nome Consumidor"].map(normaliza))
juntos["codigo_cs"] = juntos["Código da Cozinha"].where(juntos["Código da Cozinha"].astype(str).str.startswith("CS"))

# Cada variante: (linhas usadas, coluna que identifica a "cozinha")
variantes = {
    "codigo_todos": (juntos, "Código da Cozinha"),                                      # medida principal (D-3)
    "codigo_so_cds": (juntos[juntos["MECANISMO"] == "CDS/COZINHAS"], "Código da Cozinha"),  # tira CDAF/CI (zeros de outra modalidade)
    "nome_todos": (juntos, "nome_norm"),                                                # teto: nomes de consumidor normalizados
    "codigo_sem_eg_ug": (juntos, "codigo_cs"),                                          # só códigos CS (sem EG e "unidade gestora")
}

linhas = []
for variante, (dados, coluna) in variantes.items():
    grau = dados.groupby("CNPJ")[coluna].nunique()
    n = len(grau)
    n_top = int(round(0.10 * n))
    media, mediana = grau.mean(), grau.median()
    participacao_top = grau.sort_values(ascending=False).head(n_top).sum() / grau.sum()
    referencia_ok = (media - mediana >= 1) and (participacao_top >= 0.20)  # referência fixada em D-5
    linhas += [
        (variante, "n_organizacoes", n),
        (variante, "n_vinculos", int(grau.sum())),
        (variante, "mediana", round(mediana, 1)),
        (variante, "media", round(media, 2)),
        (variante, "media_menos_mediana", round(media - mediana, 2)),
        (variante, "n_top10pct", n_top),
        (variante, "participacao_top10pct", round(participacao_top, 3)),
        (variante, "prop_0", round((grau == 0).mean(), 3)),
        (variante, "prop_1", round((grau == 1).mean(), 3)),
        (variante, "prop_10_ou_mais", round((grau >= 10).mean(), 3)),
        (variante, "maximo", int(grau.max())),
        (variante, "referencia_D5_atendida", int(referencia_ok)),
    ]

# Cobertura: quantos projetos têm ao menos uma unidade recebedora registrada
linhas += [
    ("cobertura", "n_projetos", contratacoes["N° DO PROJETO"].nunique()),
    ("cobertura", "prop_projetos_com_unidade", round(contratacoes["N° DO PROJETO"].isin(unidades["Num TPAF"]).mean(), 3)),
    ("cobertura", "n_linhas_unidades", len(unidades)),
]

SAIDA.parent.mkdir(parents=True, exist_ok=True)
pd.DataFrame(linhas, columns=["variante", "metrica", "valor"]).to_csv(SAIDA, index=False)
print(pd.DataFrame(linhas, columns=["variante", "metrica", "valor"]).pivot(index="metrica", columns="variante", values="valor").to_string())
