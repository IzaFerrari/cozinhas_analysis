# Exploração 2026-10-21 (D-4), DATA1, papel discovery. Economia de rota e pool por UF.
import sys, numpy as np, pandas as pd
base = sys.argv[1]
c = pd.read_csv(f"{base}/contratacoes.csv", header=10, dtype=str)
u = pd.read_csv(f"{base}/unidades.csv", header=6, dtype=str)
u["cod"] = u["Código da Cozinha"].str.strip()
cds = c[c["MECANISMO RESUMO 2"] == "CDS"]
e = cds[["N° DO PROJETO", "CNPJ", "UF ORGANIZAÇÃO", "CÓDIGO IBGE"]].merge(
    u[["Num TPAF", "cod", "Cod IBGE Consumidor", "UF Consumidor"]], left_on="N° DO PROJETO", right_on="Num TPAF").drop_duplicates(["CNPJ", "cod"])
# polo = município com mais unidades vinculadas na UF (proxy interno; não usa lista de capitais)
mu = e.drop_duplicates("cod").groupby(["UF Consumidor", "Cod IBGE Consumidor"]).size().rename("n").reset_index()
polo = mu.sort_values("n").groupby("UF Consumidor").tail(1).set_index("UF Consumidor")["Cod IBGE Consumidor"]
e["no_polo"] = e["Cod IBGE Consumidor"] == e["UF Consumidor"].map(polo)
e["mesmo_mun"] = e["CÓDIGO IBGE"] == e["Cod IBGE Consumidor"]
o = e.groupby("CNPJ").agg(uf=("UF ORGANIZAÇÃO", "first"), grau=("cod", "nunique"), nmun=("Cod IBGE Consumidor", "nunique"),
                          polo=("no_polo", "mean"), mesmo=("mesmo_mun", "mean"))
o["unid_por_mun"] = o["grau"] / o["nmun"]
print("== rota: por faixa de grau (CDS, grau>0)")
print(o.groupby(pd.cut(o["grau"], [0, 1, 3, 9, 99]))[["nmun", "unid_por_mun", "polo", "mesmo"]].agg(["median", "mean"]).round(2).to_string())
print("fração de vínculos no próprio município: %.2f | no polo da UF: %.2f" % (e["mesmo_mun"].mean(), e["no_polo"].mean()))
print("concentração das unidades: fração das unidades da UF no polo")
print(mu.groupby("UF Consumidor")["n"].apply(lambda s: round(s.max() / s.sum(), 2)).sort_values(ascending=False).to_dict())
print("rank corr grau~nmun %.2f, grau~unid_por_mun %.2f" % (o["grau"].rank().corr(o["nmun"].rank()), o["grau"].rank().corr(o["unid_por_mun"].rank())))

# pool: o conjunto de cada organização cobre que fração do conjunto de unidades da UF?
uf_set = e.groupby("UF ORGANIZAÇÃO")["cod"].apply(set)
o["cobre_uf"] = [len(set(e.loc[e["CNPJ"] == k, "cod"])) / len(uf_set[o.loc[k, "uf"]]) for k in o.index]
print("\n== pool: cobertura do conjunto da UF por organização (mediana), e nº de orgs que cobrem >=80%")
t = o.groupby("uf").agg(orgs=("grau", "size"), cob_med=("cobre_uf", "median"), orgs_80=("cobre_uf", lambda s: int((s >= 0.8).sum())))
t["unid"] = uf_set.map(len).reindex(t.index)
print(t.sort_values("cob_med", ascending=False).to_string())
# segmento do nº do projeto (chamada?) e unidades previstas idênticas dentro da UF
cds = cds.assign(seg=cds["N° DO PROJETO"].str.split("/").str[2], uprev=cds["Nº. DE ATENDIMENTO ÀS UNIDADES RECEBEDORAS PREVISTO*"])
print("\n== variedade do nº previsto de unidades dentro da UF (CDS): nº de valores distintos / nº de projetos")
print(cds.groupby("UF ORGANIZAÇÃO").apply(lambda d: f"{d['uprev'].nunique()}/{len(d)}", include_groups=False).to_dict())
