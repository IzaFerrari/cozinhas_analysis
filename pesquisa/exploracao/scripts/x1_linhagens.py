# Exploração 2026-10-21 (D-4), DATA1, papel discovery. Sinais das linhagens candidatas.
import sys, unicodedata, re
import numpy as np, pandas as pd
def spearmanr(a, b, nan_policy=None):
    class R: pass
    r = R(); d = pd.DataFrame({"a": pd.Series(a).values, "b": pd.Series(b).values}).replace([np.inf, -np.inf], np.nan).dropna().rank()
    r.statistic = d["a"].corr(d["b"]); return r
base = sys.argv[1]
c = pd.read_csv(f"{base}/contratacoes.csv", header=10, dtype=str)
u = pd.read_csv(f"{base}/unidades.csv", header=6, dtype=str)
def num(s):
    s = s.fillna("").str.strip().str.replace(".", "", regex=False).str.replace(",", ".", regex=False)
    return pd.to_numeric(s.replace({"-": None, "": None}), errors="coerce")
c["valor"] = num(c["VALOR TOTAL PREVISTO(R$)"]); c["kg"] = num(c["QUANTIDADE PREVISTA (KG)"])
c["nforn"] = num(c["Nº.  FORNECEDORES PREVISTO*"]); c["uprev"] = num(c["Nº. DE ATENDIMENTO ÀS UNIDADES RECEBEDORAS PREVISTO*"])
c["benef"] = num(c["Nº.  TOTAL ATENDIMENTO A BENEFICIÁRIOS CONSUMIDORES PREVISTO*"])
u["atend"] = num(u["Qtd Total Atendidos"])
u["cod"] = u["Código da Cozinha"].str.strip()
c["mec"] = c["MECANISMO RESUMO 2"]

# --- planejado × registrado, por projeto
reg = u.groupby("Num TPAF")["cod"].nunique()
c["ureg"] = c["N° DO PROJETO"].map(reg).fillna(0)
print("== L5 planejado × registrado (por projeto)")
for m, g in c.groupby("mec"):
    ok = g["uprev"].notna()
    print(m, "n=", len(g), "com previsto=", ok.sum(), "iguais=", (g.loc[ok, "uprev"] == g.loc[ok, "ureg"]).sum(),
          "reg>prev=", (g.loc[ok, "ureg"] > g.loc[ok, "uprev"]).sum(), "reg<prev=", (g.loc[ok, "ureg"] < g.loc[ok, "uprev"]).sum())

cds = c[c["mec"] == "CDS"]
e = cds[["N° DO PROJETO", "CNPJ", "UF ORGANIZAÇÃO", "CÓDIGO IBGE"]].merge(
    u[["Num TPAF", "cod", "UF Consumidor", "Cod IBGE Consumidor", "Ind CNPJ Proprio", "Entidade Cedente CNPJ", "CNPJ Consumidor", "atend"]],
    left_on="N° DO PROJETO", right_on="Num TPAF")
org = cds.groupby("CNPJ").agg(uf=("UF ORGANIZAÇÃO", "first"), valor=("valor", "sum"), kg=("kg", "sum"),
                              nforn=("nforn", "sum"), nproj=("N° DO PROJETO", "nunique"))
org["grau"] = e.groupby("CNPJ")["cod"].nunique().reindex(org.index).fillna(0)
print("\n== base CDS: orgs", len(org), "vínculos", int(org["grau"].sum()))

# --- L1 capacidade ÷ demanda
ua = u.drop_duplicates("cod").set_index("cod")["atend"]
org["atend_med"] = e.drop_duplicates(["CNPJ", "cod"]).assign(a=lambda d: d["cod"].map(ua)).groupby("CNPJ")["a"].median()
g = org[org["grau"] > 0]
print("\n== L1 capacidade/demanda (orgs CDS com grau>0, n=%d)" % len(g))
for col in ["valor", "kg", "nforn", "atend_med"]:
    r = spearmanr(g["grau"], g[col], nan_policy="omit"); print(f"rho(grau,{col}) = {r.statistic:.2f}")
r = spearmanr(g["grau"], g["kg"] / g["atend_med"], nan_policy="omit"); print(f"rho(grau, kg/atend_med) = {r.statistic:.2f}")
g2 = g.assign(kg_por_vinc=g["kg"] / g["grau"], valor_por_vinc=g["valor"] / g["grau"])
print("kg por vínculo: mediana por faixa de grau")
print(g2.groupby(pd.cut(g2["grau"], [0, 1, 3, 9, 99]))[["kg_por_vinc", "valor_por_vinc", "atend_med"]].median().round(0).to_string())

# --- L2 regra de alocação: pooling (biclique) × pareamento
print("\n== L2 conjuntos idênticos de unidades entre organizações (CDS)")
sets = e.groupby("CNPJ")["cod"].apply(lambda s: tuple(sorted(set(s))))
sets = sets[sets.str.len() >= 2]
dup = sets.value_counts(); clones = dup[dup >= 2]
print("orgs com grau>=2:", len(sets), "| conjuntos repetidos:", len(clones), "| orgs em conjuntos repetidos:", int(clones.sum()))
k = e.drop_duplicates(["CNPJ", "cod"]).merge(org[["uf"]], left_on="CNPJ", right_index=True)
rows = []
for uf, d in k.groupby("uf"):
    no, nu, ne = d["CNPJ"].nunique(), d["cod"].nunique(), len(d)
    s = sets[sets.index.isin(d["CNPJ"].unique())]
    rows.append(dict(uf=uf, orgs=no, unid=nu, vinc=ne, dens=round(ne / (no * nu), 2),
                     orgs_por_unid=round(ne / nu, 1), orgs_em_clone=int(s.map(s.value_counts()).ge(2).sum())))
t = pd.DataFrame(rows).sort_values("dens", ascending=False); print(t.to_string(index=False))

# --- L3 perecibilidade
def norm(x): return unicodedata.normalize("NFKD", str(x)).encode("ascii", "ignore").decode().upper()
PER = r"HORT|FRUT|VERDUR|LEGUM|BANANA|ALFACE|TOMATE|PESCADO|PEIXE|TILAPIA|CARNE|FRANGO|OVO|LEITE(?! EM PO)|QUEIJO|IOGURTE|POLPA|ABOBORA|MAMAO|LARANJA|MELANCIA"
NPER = r"ARROZ|FEIJ|FARINHA|CAFE|ACUCAR|MEL\b|LEITE EM PO|CASTANHA|FUBA|MILHO|BISCOITO|PROCESSADO|DOCE|RAPADURA|GOMA|TAPIOCA|OLEO|MASSA"
cds = cds.assign(p=cds["PRODUTOS PREVISTOS NOS PROJETOS"].map(norm))
cds = cds.assign(per=cds["p"].str.contains(PER), nper=cds["p"].str.contains(NPER))
cat = cds.groupby("CNPJ").agg(per=("per", "any"), nper=("nper", "any"))
org["cesta"] = np.select([cat["per"] & ~cat["nper"], ~cat["per"] & cat["nper"], cat["per"] & cat["nper"]],
                         ["só perecível", "só não perecível", "misto"], "não classificado")
print("\n== L3 perecibilidade (CDS)"); print(org.groupby("cesta")["grau"].describe()[["count", "50%", "mean", "75%", "max"]].round(1).to_string())
inter = e.assign(fora=e["UF ORGANIZAÇÃO"] != e["UF Consumidor"]).drop_duplicates(["CNPJ", "cod"]).merge(org[["cesta"]], left_on="CNPJ", right_index=True)
print("vínculos interestaduais por cesta:"); print(inter.groupby("cesta")["fora"].agg(["sum", "count"]).to_string())
mun = e.assign(mesmo=e["CÓDIGO IBGE"].str.strip() == e["Cod IBGE Consumidor"].str.strip()).drop_duplicates(["CNPJ", "cod"])
org["nmun"] = e.groupby("CNPJ")["Cod IBGE Consumidor"].nunique().reindex(org.index)
org["mesmo_mun"] = mun.groupby("CNPJ")["mesmo"].mean().reindex(org.index)
print("municípios atendidos e fração no mesmo município, por cesta:")
print(org[org["grau"] > 0].groupby("cesta")[["nmun", "mesmo_mun"]].median().round(2).to_string())

# --- L4 guarda-chuva (entidade cedente)
print("\n== L4 entidade cedente")
e["contraparte"] = np.where(e["Ind CNPJ Proprio"].str.strip() == "NAO", e["Entidade Cedente CNPJ"].str.strip(), e["CNPJ Consumidor"].str.strip())
ced = e[e["Ind CNPJ Proprio"].str.strip() == "NAO"].drop_duplicates("cod")
print("unidades CDS sem CNPJ próprio:", len(ced), "de", e["cod"].nunique(), "| cedentes distintos:", ced["Entidade Cedente CNPJ"].nunique())
print("maiores cedentes (nº de unidades):", ced["Entidade Cedente CNPJ"].value_counts().head(6).to_dict())
org["n_contraparte"] = e.groupby("CNPJ")["contraparte"].nunique().reindex(org.index)
org["frac_sem_cnpj"] = e.drop_duplicates(["CNPJ", "cod"]).assign(n=lambda d: d["Ind CNPJ Proprio"].str.strip() == "NAO").groupby("CNPJ")["n"].mean().reindex(org.index)
g = org[org["grau"] > 0]
print("grau × contrapartes: mediana grau %.0f, mediana contrapartes %.0f; rho(grau, frac_sem_cnpj) = %.2f" % (
    g["grau"].median(), g["n_contraparte"].median(), spearmanr(g["grau"], g["frac_sem_cnpj"]).statistic))
print(g.groupby(pd.cut(g["grau"], [0, 1, 3, 9, 99]))[["n_contraparte", "frac_sem_cnpj"]].median().round(2).to_string())
print("por UF (frac de unidades sem CNPJ próprio):")
print(e.drop_duplicates("cod").groupby("UF Consumidor")["Ind CNPJ Proprio"].apply(lambda s: round((s.str.strip() == "NAO").mean(), 2)).sort_values(ascending=False).head(10).to_dict())
org.to_csv(sys.argv[2])
