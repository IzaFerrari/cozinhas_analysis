import sys, re
import numpy as np
import pandas as pd

D = sys.argv[1]
pd.set_option("display.width", 220); pd.set_option("display.max_columns", 40); pd.set_option("display.max_rows", 200)

c = pd.read_csv(f"{D}/contratacoes.csv", header=10)
u = pd.read_csv(f"{D}/unidades.csv", header=6)

def num(s):
    return pd.to_numeric(s.astype(str).str.replace(r"[R$\s]", "", regex=True).str.replace(".", "", regex=False).str.replace(",", ".", regex=False), errors="coerce")

c["valor"] = num(c["VALOR TOTAL PREVISTO(R$)"])
c["n_forn"] = pd.to_numeric(c["Nº.  FORNECEDORES PREVISTO*"], errors="coerce")
c["n_ur_prev"] = num(c["Nº. DE ATENDIMENTO ÀS UNIDADES RECEBEDORAS PREVISTO*"])
c["n_benef_prev"] = num(c["Nº.  TOTAL ATENDIMENTO A BENEFICIÁRIOS CONSUMIDORES PREVISTO*"])
c["kg"] = c["QUANTIDADE PREVISTA (KG)"]
c["modal"] = c["N° DO PROJETO"].str.split("/").str[2]

print("== MECANISMO x modalidade no nº do projeto")
print(pd.crosstab(c["MECANISMO"], c["modal"]))
semcoz = ~c["N° DO PROJETO"].isin(u["Num TPAF"])
print("\n== projetos sem cozinha por MECANISMO / UF")
print(pd.crosstab(c["MECANISMO"], semcoz))
print(c.loc[semcoz, "UF ORGANIZAÇÃO"].value_counts().to_dict())
print("\n== valor parse check", c["valor"].describe().round(0).to_dict(), c["VALOR TOTAL PREVISTO(R$)"].head(3).tolist())
print("n_ur_prev parse", c["Nº. DE ATENDIMENTO ÀS UNIDADES RECEBEDORAS PREVISTO*"].head(5).tolist())

# ---- códigos de cozinha
code = u["Código da Cozinha"].astype(str)
print("\n== códigos que não seguem CS\\d+:")
print(code[~code.str.match(r"^CS\d+$")].value_counts())
print("\nInd CNPJ Proprio:", u["Ind CNPJ Proprio"].value_counts().to_dict())
print("Tipo Consumidor:", u["Tipo Consumidor RESUMO"].value_counts().to_dict())
# um código -> quantos CNPJ consumidor/nomes? um CNPJ consumidor -> quantos códigos?
g = u.groupby("Código da Cozinha").agg(n_cnpj=("CNPJ Consumidor", "nunique"), n_nome=("Nome Consumidor", "nunique"), n_mun=("Cod IBGE Consumidor", "nunique"))
print("\ncódigo->nº CNPJ consumidor distintos:", g["n_cnpj"].value_counts().sort_index().to_dict())
print("código->nº municípios distintos:", g["n_mun"].value_counts().sort_index().to_dict())
h = u.groupby("CNPJ Consumidor")["Código da Cozinha"].nunique()
print("CNPJ consumidor->nº códigos distintos (top):", h.sort_values(ascending=False).head(8).to_dict())
ec = u[u["Entidade Cedente CNPJ"] != "NÃO SE APLICA"].groupby("Entidade Cedente CNPJ")["Código da Cozinha"].nunique()
print("entidades cedentes:", len(ec), "| cozinhas por cedente (top):", ec.sort_values(ascending=False).head(8).to_dict())

# ---- rede bipartida org–cozinha
j = c.merge(u, left_on="N° DO PROJETO", right_on="Num TPAF", how="left")
links = j.dropna(subset=["Código da Cozinha"]).drop_duplicates(["CNPJ", "Código da Cozinha"])
deg_org = j.groupby("CNPJ")["Código da Cozinha"].nunique()
uf_org = c.groupby("CNPJ")["UF ORGANIZAÇÃO"].first()
deg_k = links.groupby("Código da Cozinha")["CNPJ"].nunique()
print("\n== grau das cozinhas (nº de organizações por cozinha):", deg_k.value_counts().sort_index().to_dict())
print("cozinhas distintas:", deg_k.size, "| ligações:", len(links))

# identidade: soma graus org = soma graus cozinha = ligações. Por UF da organização:
org = pd.DataFrame({"deg": deg_org, "uf": uf_org})
org["valor"] = c.groupby("CNPJ")["valor"].sum()
org["kg"] = c.groupby("CNPJ")["kg"].sum()
org["n_proj"] = c.groupby("CNPJ")["N° DO PROJETO"].nunique()
org["n_forn"] = c.groupby("CNPJ")["n_forn"].sum()
org["n_ur_prev"] = c.groupby("CNPJ")["n_ur_prev"].sum()
org["tipo"] = c.groupby("CNPJ")["TIPO ORGANIZAÇÃO"].first()
org["prod"] = c.groupby("CNPJ")["PRODUTOS PREVISTOS NOS PROJETOS"].agg(lambda s: "|".join(sorted(set(s.dropna()))))
org["nome"] = c.groupby("CNPJ")["ORGANIZAÇÃO FORNECEDORA"].first()

# cozinhas por UF (da cozinha) e orgs por UF
k_uf = u.drop_duplicates("Código da Cozinha").groupby("UF Consumidor").size()
st = org.groupby("uf").agg(n_org=("deg", "size"), med_deg=("deg", "median"), mean_deg=("deg", "mean"), valor_med=("valor", "median"), proj_por_org=("n_proj", "mean"))
st["n_coz_UF"] = k_uf.reindex(st.index).fillna(0).astype(int)
st["coz_por_org"] = (st["n_coz_UF"] / st["n_org"]).round(2)
# multi-homing das cozinhas por UF da cozinha
kuf = u.drop_duplicates("Código da Cozinha").set_index("Código da Cozinha")["UF Consumidor"]
st["orgs_por_coz"] = deg_k.groupby(kuf.reindex(deg_k.index)).mean().reindex(st.index).round(2)
st["valor_por_lig"] = (org.groupby("uf")["valor"].sum() / org.groupby("uf")["deg"].sum()).round(0)
print("\n== por UF")
print(st.sort_values("mean_deg", ascending=False))
print("\ncorr(log coz_por_org, log mean_deg) entre UFs:",
      np.corrcoef(np.log(st["coz_por_org"].clip(lower=0.1)), np.log(st["mean_deg"].clip(lower=0.1)))[0, 1].round(3))

# decomposição de variância entre/dentro de UF
gm = org["deg"].mean()
ss_tot = ((org["deg"] - gm) ** 2).sum()
ss_bet = (org.groupby("uf")["deg"].transform("mean") - gm).pow(2).sum()
print("\n== eta² (UF explica variância do grau):", round(ss_bet / ss_tot, 3))
lg = np.log1p(org["deg"])
print("eta² em log1p:", round(((lg.groupby(org["uf"]).transform("mean") - lg.mean()) ** 2).sum() / ((lg - lg.mean()) ** 2).sum(), 3))

# escala: valor vs grau
pos = org[(org["deg"] > 0) & (org["valor"] > 0)]
print("\n== corr Spearman grau x valor:", round(pos["deg"].rank().corr(pos["valor"].rank()), 3),
      "| grau x kg:", round(pos["deg"].rank().corr(pos["kg"].rank()), 3),
      "| grau x n_proj:", round(pos["deg"].rank().corr(pos["n_proj"].rank()), 3),
      "| grau x n_forn:", round(pos["deg"].rank().corr(pos["n_forn"].rank()), 3),
      "| grau x n_ur_prev:", round(pos["deg"].rank().corr(pos["n_ur_prev"].rank()), 3))
b = np.polyfit(np.log(pos["valor"]), np.log(pos["deg"]), 1)
print("elasticidade log(grau)~log(valor):", b.round(3))
print("valor por org: describe", pos["valor"].describe().round(0).to_dict())
print("valor por projeto: value_counts top", c["valor"].round(-3).value_counts().head(8).to_dict())
# previsto vs observado por projeto
kp = u.groupby("Num TPAF")["Código da Cozinha"].nunique()
cp = c.set_index("N° DO PROJETO")[["n_ur_prev", "valor", "UF ORGANIZAÇÃO"]].copy()
cp["obs"] = kp.reindex(cp.index).fillna(0)
print("\n== UR previsto vs cozinhas observadas por projeto: Spearman", round(cp["n_ur_prev"].rank().corr(cp["obs"].rank()), 3))
print((cp["n_ur_prev"] - cp["obs"]).describe().round(2).to_dict())
print("cozinhas/projeto por UF (mediana):", cp.groupby("UF ORGANIZAÇÃO")["obs"].median().sort_values(ascending=False).head(8).to_dict())

# tipo de produto
org["prod_main"] = org["prod"].str.split("|").str[0]
print("\n== grau por produto (orgs com 1 tipo de produto)")
print(org.groupby("prod").agg(n=("deg", "size"), med=("deg", "median"), mean=("deg", "mean"), p90=("deg", lambda s: s.quantile(.9))).sort_values("n", ascending=False).head(15))
print("\n== grau por tipo de organização")
print(org.groupby("tipo")["deg"].describe()[["count", "50%", "mean", "max"]])

# nomes: reforma agrária / assentados / MST
ra = org["nome"].str.upper().str.contains(r"REFORMA|ASSENTAD|ASSENTAMENT", regex=True)
print("\n== org com 'reforma/assentad' no nome:", ra.sum(), "| mediana grau", org.loc[ra, "deg"].median(), "vs", org.loc[~ra, "deg"].median(),
      "| média", round(org.loc[ra, "deg"].mean(), 2), "vs", round(org.loc[~ra, "deg"].mean(), 2))
print(org.loc[ra].groupby("uf")["deg"].agg(["size", "median"]).sort_values("size", ascending=False).head(10).T)

# geografia: municípios distintos atendidos por org, % ligações no mesmo município
j2 = j.dropna(subset=["Código da Cozinha"]).copy()
j2["mesmo_mun"] = j2["CÓDIGO IBGE"] == j2["Cod IBGE Consumidor"]
geo = j2.groupby("CNPJ").agg(n_mun=("Cod IBGE Consumidor", "nunique"), mesmo=("mesmo_mun", "mean"))
org = org.join(geo)
print("\n== geografia: Spearman grau x nº municípios das cozinhas:", round(org["deg"].rank().corr(org["n_mun"].rank()), 3))
print("% ligações em que cozinha está no município da org:", round(j2.drop_duplicates(["CNPJ", "Código da Cozinha"])["mesmo_mun"].mean(), 3))
print(org.groupby(pd.cut(org["deg"], [-1, 0, 1, 3, 8, 30]))[["n_mun", "mesmo"]].mean().round(2))

# top 15 orgs, detalhes
print("\n== top 15")
print(org.sort_values("deg", ascending=False).head(15)[["uf", "deg", "n_proj", "valor", "kg", "n_forn", "n_ur_prev", "n_mun", "mesmo", "tipo", "prod"]])

# kitchens in AL/PB/RN: degree and names
for uf in ["AL", "PB", "RN"]:
    kk = deg_k[kuf.reindex(deg_k.index) == uf]
    print(f"\n{uf}: cozinhas {kk.size}, orgs por cozinha {kk.value_counts().sort_index().to_dict()}")

org.to_csv(f"{D}/../org_features.csv")
links.to_csv(f"{D}/../links.csv", index=False)
