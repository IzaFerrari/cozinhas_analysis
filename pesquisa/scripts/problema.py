# Gate 1B (D-6): premissas P1 e P2 em DATA1, projetos CDS. Uso: problema.py <brutos> <saida.csv>
import sys, hashlib
import pandas as pd

base, saida = sys.argv[1], sys.argv[2]
SHA = {"contratacoes.csv": "480b46c4660add2d8f8f64b1206bd04c05a85e21432b4cc5b9103879ebd31dbc",
       "unidades.csv": "6754d7152e46ded005c27e61072420b40710a80bec86be79b3184fd0bc1db102"}
for nome, h in SHA.items():  # DATA1 (D-1): para se o arquivo não for o snapshot registrado
    assert hashlib.sha256(open(f"{base}/{nome}", "rb").read()).hexdigest() == h, nome

c = pd.read_csv(f"{base}/contratacoes.csv", header=10, dtype=str)
u = pd.read_csv(f"{base}/unidades.csv", header=6, dtype=str)
u["cod"] = u["Código da Cozinha"].str.strip()
cds = c[c["MECANISMO RESUMO 2"] == "CDS"]
v = (cds[["N° DO PROJETO", "CNPJ", "UF ORGANIZAÇÃO"]]
     .merge(u[["Num TPAF", "cod"]], left_on="N° DO PROJETO", right_on="Num TPAF")
     .drop_duplicates(["CNPJ", "cod"]))
linhas = []
def add(premissa, escopo, metrica, valor):
    linhas.append(dict(premissa=premissa, escopo=escopo, metrica=metrica, valor=valor))

# P1: heterogeneidade do grau entre organizações CDS com ao menos uma unidade
grau = v.groupby("CNPJ")["cod"].nunique().sort_values(ascending=False)
n_top = round(0.10 * len(grau))
add("P1", "BR", "organizacoes", len(grau))
add("P1", "BR", "vinculos", int(grau.sum()))
add("P1", "BR", "media", round(grau.mean(), 2))
add("P1", "BR", "mediana", grau.median())
add("P1", "BR", "media_menos_mediana", round(grau.mean() - grau.median(), 2))
add("P1", "BR", "top10_organizacoes", n_top)
add("P1", "BR", "top10_participacao", round(grau.head(n_top).sum() / grau.sum(), 3))
add("P1", "BR", "maximo", int(grau.max()))

# P2: componentes conexos do grafo organização–código, por UF elegível
def componentes(arestas):
    pai = {}
    def raiz(x):
        while pai.setdefault(x, x) != x:
            pai[x] = pai[pai[x]]; x = pai[x]
        return x
    for o, k in arestas:
        pai[raiz(("o", o))] = raiz(("u", k))
    return {n: raiz(n) for n in pai}

for uf, d in v.groupby("UF ORGANIZAÇÃO"):
    n_org, n_uni = d["CNPJ"].nunique(), d["cod"].nunique()
    if n_uni < 10 or n_org < 3:
        continue
    comp = componentes(zip(d["CNPJ"], d["cod"]))
    d = d.assign(comp=[comp[("o", o)] for o in d["CNPJ"]])
    resumo = d.groupby("comp").agg(orgs=("CNPJ", "nunique"), unid=("cod", "nunique"), vinc=("cod", "size"))
    resumo["dens"] = resumo["vinc"] / (resumo["orgs"] * resumo["unid"])
    pool = resumo[(resumo["orgs"] >= 2) & (resumo["dens"] >= 0.5)]["vinc"].sum()
    exclusivo = resumo[resumo["orgs"] == 1]["vinc"].sum()
    maior = resumo.sort_values("vinc").iloc[-1]
    add("P2", uf, "organizacoes", n_org)
    add("P2", uf, "unidades", n_uni)
    add("P2", uf, "vinculos", len(d))
    add("P2", uf, "unidades_por_organizacao", round(n_uni / n_org, 2))
    add("P2", uf, "componentes", len(resumo))
    add("P2", uf, "participacao_pool", round(pool / len(d), 2))
    add("P2", uf, "participacao_exclusiva", round(exclusivo / len(d), 2))
    add("P2", uf, "maior_componente_orgs", int(maior["orgs"]))
    add("P2", uf, "maior_componente_unid", int(maior["unid"]))
    add("P2", uf, "maior_componente_dens", round(maior["dens"], 2))

pd.DataFrame(linhas).to_csv(saida, index=False)
