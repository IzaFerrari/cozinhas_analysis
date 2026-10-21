# Exploração 2026-10-21 (D-4), DATA1, papel discovery. Densidade no destino sem as unidades da própria organização.
import sys, numpy as np, pandas as pd
base, orgcsv = sys.argv[1], sys.argv[2]
c = pd.read_csv(f"{base}/contratacoes.csv", header=10, dtype=str)
u = pd.read_csv(f"{base}/unidades.csv", header=6, dtype=str)
u["cod"] = u["Código da Cozinha"].str.strip()
cds = c[c["MECANISMO RESUMO 2"] == "CDS"]
e = cds[["N° DO PROJETO", "CNPJ", "UF ORGANIZAÇÃO"]].merge(u[["Num TPAF", "cod", "Cod IBGE Consumidor"]],
     left_on="N° DO PROJETO", right_on="Num TPAF").drop_duplicates(["CNPJ", "cod"])
mun_units = e.groupby("Cod IBGE Consumidor")["cod"].apply(set)
own = e.groupby("CNPJ")["cod"].apply(set)
o = pd.read_csv(orgcsv, index_col=0); o = o[o["grau"] > 0].copy()
uf_set = e.groupby("UF ORGANIZAÇÃO")["cod"].apply(set)
o["cobre_uf"] = [len(own[k]) / len(uf_set[o.loc[k, "uf"]]) for k in o.index]
reg = o.groupby("uf")["cobre_uf"].median()
def outros(k):
    muns = e.loc[e["CNPJ"] == k, "Cod IBGE Consumidor"].unique()
    return np.median([len(mun_units[m] - own[k]) for m in muns])
o["dens_outros"] = [outros(k) for k in o.index]
p = o[o["uf"].map(reg) < 0.5]
print("partição n=%d: rho(grau, unidades de outras orgs nos destinos) = %.2f" % (len(p), p["grau"].rank().corr(p["dens_outros"].rank())))
print(p.groupby(pd.cut(p["grau"], [0, 1, 3, 9, 99]))["dens_outros"].agg(["median", "mean", "size"]).round(1).to_string())
