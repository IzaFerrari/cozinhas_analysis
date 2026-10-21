# Fase 4: qualidade da ligação e população analítica de DATA1. Uso: dados.py <brutos> <saida.csv>
import sys, hashlib
import pandas as pd

base, saida = sys.argv[1], sys.argv[2]
SHA = {"contratacoes.csv": "480b46c4660add2d8f8f64b1206bd04c05a85e21432b4cc5b9103879ebd31dbc",
       "unidades.csv": "6754d7152e46ded005c27e61072420b40710a80bec86be79b3184fd0bc1db102"}
for nome, h in SHA.items():  # DATA1 (D-1)
    assert hashlib.sha256(open(f"{base}/{nome}", "rb").read()).hexdigest() == h, nome
c = pd.read_csv(f"{base}/contratacoes.csv", header=10, dtype=str)
u = pd.read_csv(f"{base}/unidades.csv", header=6, dtype=str)
u["cod"] = u["Código da Cozinha"].str.strip()
linhas = []
def add(bloco, metrica, valor):
    linhas.append(dict(bloco=bloco, metrica=metrica, valor=valor))

add("contratacoes", "linhas", len(c))
add("contratacoes", "projetos_distintos", c["N° DO PROJETO"].nunique())
add("contratacoes", "cnpjs_distintos", c["CNPJ"].nunique())
add("contratacoes", "cnpjs_com_mais_de_um_nome", int((c.groupby("CNPJ")["ORGANIZAÇÃO FORNECEDORA"].nunique() > 1).sum()))
add("contratacoes", "cnpjs_em_mais_de_uma_uf", int((c.groupby("CNPJ")["UF ORGANIZAÇÃO"].nunique() > 1).sum()))
for m, n in c["MECANISMO RESUMO 2"].value_counts().items():
    add("contratacoes", f"projetos_{m}", int(n))
add("unidades", "linhas", len(u))
add("unidades", "codigo_ausente", int(u["cod"].isna().sum()))
add("unidades", "codigos_distintos", u["cod"].nunique())
add("unidades", "linhas_duplicadas_projeto_codigo", int(u.duplicated(["Num TPAF", "cod"]).sum()))
add("ligacao", "linhas_unidades_com_projeto", int(u["Num TPAF"].isin(c["N° DO PROJETO"]).sum()))
add("ligacao", "projetos_com_unidade", int(c["N° DO PROJETO"].isin(u["Num TPAF"]).sum()))
add("ligacao", "proporcao_projetos_com_unidade", round(float(c["N° DO PROJETO"].isin(u["Num TPAF"]).mean()), 3))

cds = c[c["MECANISMO RESUMO 2"] == "CDS"]
v = (cds[["N° DO PROJETO", "CNPJ", "UF ORGANIZAÇÃO"]]
     .merge(u[["Num TPAF", "cod", "UF Consumidor"]], left_on="N° DO PROJETO", right_on="Num TPAF")
     .drop_duplicates(["CNPJ", "cod"]))
add("cds", "projetos", len(cds))
add("cds", "projetos_com_unidade", int(cds["N° DO PROJETO"].isin(u["Num TPAF"]).sum()))
add("cds", "organizacoes", cds["CNPJ"].nunique())
add("cds", "organizacoes_com_vinculo", v["CNPJ"].nunique())
add("cds", "organizacoes_com_mais_de_um_projeto", int((cds.groupby("CNPJ")["N° DO PROJETO"].nunique() > 1).sum()))
add("cds", "vinculos", len(v))
add("cds", "codigos_distintos", v["cod"].nunique())
tipo = v["cod"].str.upper().str[:2].where(v["cod"].str.upper().str[:2].isin(["CS", "EG"]), "outro")
for t, n in tipo.value_counts().items():
    add("cds", f"vinculos_codigo_{t}", int(n))
add("cds", "proporcao_vinculos_nao_cs", round(float((tipo != "CS").mean()), 3))
add("cds", "vinculos_interestaduais", int((v["UF Consumidor"].str.strip() != v["UF ORGANIZAÇÃO"].str.strip()).sum()))
add("cds", "proporcao_interestadual", round(float((v["UF Consumidor"].str.strip() != v["UF ORGANIZAÇÃO"].str.strip()).mean()), 3))
add("cds", "codigos_em_mais_de_uma_uf_de_organizacao", int((v.groupby("cod")["UF ORGANIZAÇÃO"].nunique() > 1).sum()))
prev = pd.to_numeric(cds["Nº. DE ATENDIMENTO ÀS UNIDADES RECEBEDORAS PREVISTO*"], errors="coerce")
reg = cds["N° DO PROJETO"].map(u.groupby("Num TPAF")["cod"].nunique()).fillna(0)
add("cds", "previsto_ausente", int(prev.isna().sum()))
add("cds", "projetos_registrado_igual_previsto", int((reg == prev).sum()))
add("cds", "projetos_registrado_menor_previsto", int((reg < prev).sum()))
add("cds", "projetos_registrado_maior_previsto", int((reg > prev).sum()))
pd.DataFrame(linhas).to_csv(saida, index=False)
