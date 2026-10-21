# Exploração 2026-10-21 (D-4), DATA1, papel discovery. Rota e perecibilidade dentro do regime de partição; perda planejado→registrado.
import sys, numpy as np, pandas as pd
base, orgcsv = sys.argv[1], sys.argv[2]
c = pd.read_csv(f"{base}/contratacoes.csv", header=10, dtype=str)
u = pd.read_csv(f"{base}/unidades.csv", header=6, dtype=str)
u["cod"] = u["Código da Cozinha"].str.strip()
cds = c[c["MECANISMO RESUMO 2"] == "CDS"].copy()
cds["uprev"] = pd.to_numeric(cds["Nº. DE ATENDIMENTO ÀS UNIDADES RECEBEDORAS PREVISTO*"], errors="coerce")
cds["ureg"] = cds["N° DO PROJETO"].map(u.groupby("Num TPAF")["cod"].nunique()).fillna(0)
cds["perda"] = cds["uprev"] - cds["ureg"]
print("== perda previsto→registrado (CDS): por faixa de previsto")
print(cds.groupby(pd.cut(cds["uprev"], [0, 1, 3, 9, 99])).agg(proj=("perda", "size"), com_perda=("perda", lambda s: int((s > 0).sum())),
      perda_tot=("perda", "sum"), prev_tot=("uprev", "sum")).to_string())
e = cds[["N° DO PROJETO", "CNPJ", "UF ORGANIZAÇÃO"]].merge(u[["Num TPAF", "cod", "Cod IBGE Consumidor", "UF Consumidor"]],
     left_on="N° DO PROJETO", right_on="Num TPAF").drop_duplicates(["CNPJ", "cod"])
uf_set = e.groupby("UF ORGANIZAÇÃO")["cod"].apply(set)
o = pd.read_csv(orgcsv, index_col=0)
o = o[o["grau"] > 0].copy()
o["cobre_uf"] = [e.loc[e["CNPJ"] == k, "cod"].nunique() / len(uf_set[o.loc[k, "uf"]]) for k in o.index]
reg = o.groupby("uf")["cobre_uf"].median()
o["regime"] = np.where(o["uf"].map(reg) >= 0.5, "pool", "partição")
print("\n== regime por UF (mediana da cobertura >= 0,5 → pool):", sorted(reg[reg >= 0.5].index))
print(o.groupby("regime").agg(orgs=("grau", "size"), grau_med=("grau", "median"), grau_media=("grau", "mean"),
      kg_vinc=("kg", lambda s: np.nan), ).drop(columns="kg_vinc").to_string())
o["kg_vinc"] = o["kg"] / o["grau"]
print("kg por vínculo, mediana por regime:", o.groupby("regime")["kg_vinc"].median().round(0).to_dict())
# rota dentro da partição: densidade de unidades vinculadas no(s) município(s) de destino
dens_mun = e.drop_duplicates("cod").groupby("Cod IBGE Consumidor").size()
e["dens_dest"] = e["Cod IBGE Consumidor"].map(dens_mun)
o["dens_dest"] = e.groupby("CNPJ")["dens_dest"].median().reindex(o.index)
p = o[o["regime"] == "partição"]
print("\n== partição (n=%d): rho(grau, densidade no destino) = %.2f; rho(grau, nmun) = %.2f" % (
    len(p), p["grau"].rank().corr(p["dens_dest"].rank()), p["grau"].rank().corr(p["nmun"].rank())))
print(p.groupby(pd.cut(p["grau"], [0, 1, 3, 9, 99]))[["dens_dest", "nmun"]].median().to_string())
print("\n== perecibilidade dentro da partição")
print(p.groupby("cesta")["grau"].describe()[["count", "50%", "mean", "75%", "max"]].round(1).to_string())
print("\n== CNPJ próprio das unidades por regime (fração sem CNPJ próprio)")
print(o.groupby("regime")["frac_sem_cnpj"].mean().round(2).to_dict())
