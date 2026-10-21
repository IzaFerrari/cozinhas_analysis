import sys, numpy as np, pandas as pd
D=sys.argv[1]; pd.set_option("display.width",220); pd.set_option("display.max_rows",200); pd.set_option("display.max_colwidth",70)
c=pd.read_csv(f"{D}/contratacoes.csv",header=10); u=pd.read_csv(f"{D}/unidades.csv",header=6)
j=c.merge(u,left_on="N° DO PROJETO",right_on="Num TPAF",how="left")
nm=u.groupby("Código da Cozinha").agg(n_nome=("Nome Consumidor","nunique"),uf=("UF Consumidor","first"),n_mun=("Municipio Consumidor","nunique"))
print("== códigos com >1 nome de consumidor:"); print(nm[nm.n_nome>1].sort_values("n_nome",ascending=False).head(15))
print("total de nomes 'extra' por código CS:", (nm[nm.index.str.startswith("CS")].n_nome-1).sum())
for cnpj in ["91.360.420/0001-34","21.930.104/0001-75"]:
    s=j[j.CNPJ==cnpj]
    print(f"\n== {cnpj} ({s['UF ORGANIZAÇÃO'].iloc[0]}): códigos {s['Código da Cozinha'].nunique()}, nomes {s['Nome Consumidor'].nunique()}, municípios {s['Municipio Consumidor'].nunique()}")
    print(s.groupby("Código da Cozinha")["Nome Consumidor"].agg(lambda x: f"{x.nunique()} nomes: "+" | ".join(x.drop_duplicates().head(4))).to_string())
# normalização de nome para checar inflação por grafia
import unicodedata,re
def norm(x):
    x=unicodedata.normalize("NFKD",str(x)).encode("ascii","ignore").decode().upper()
    x=re.sub(r"[^A-Z0-9 ]"," ",x); x=re.sub(r"\b(DA|DE|DO|DAS|DOS|E)\b"," ",x); return re.sub(r"\s+"," ",x).strip()
j["nn"]=j["Nome Consumidor"].map(norm)
L=j.dropna(subset=["Código da Cozinha"])
print("\nnomes distintos brutos:",L["Nome Consumidor"].nunique(),"| normalizados:",L["nn"].nunique(),"| códigos:",L["Código da Cozinha"].nunique())
deg_code=j.groupby("CNPJ")["Código da Cozinha"].nunique(); deg_nn=L.groupby("CNPJ")["nn"].nunique().reindex(deg_code.index,fill_value=0)
uf=c.groupby("CNPJ")["UF ORGANIZAÇÃO"].first()
cmp=pd.DataFrame({"code":deg_code,"nome":deg_nn,"uf":uf})
print("\n== grau por UF: código vs nome normalizado (média)")
t=cmp.groupby("uf")[["code","nome"]].mean().round(2); t["razao"]=(t.nome/t.code).round(2); print(t.sort_values("razao",ascending=False).head(10))
print("\nRank correlation code vs nome:", round(cmp.code.rank().corr(cmp.nome.rank()),3))
print("top 10 por nome:"); print(cmp.sort_values("nome",ascending=False).head(10))
print("\nmediana/média/máx por código:",cmp.code.median(),round(cmp.code.mean(),2),cmp.code.max()," | por nome:",cmp.nome.median(),round(cmp.nome.mean(),2),cmp.nome.max())
# decompor as orgs com grau 1 e 0
def kind(x):
    x=str(x); return "CS" if x.startswith("CS") else ("EG" if x.startswith("EG") else ("UG" if x=="unidade gestora" else "sem"))
j["kind"]=j["Código da Cozinha"].map(kind)
o=j.groupby("CNPJ").agg(deg=("Código da Cozinha","nunique"),mec=("MECANISMO",lambda s:"|".join(sorted(set(s)))),kinds=("kind",lambda s:"|".join(sorted(set(s)))))
print("\n== orgs com grau 0 e 1: mecanismo e tipo de código")
for d in [0,1]:
    print(f"grau {d}:"); print(o[o.deg==d].groupby(["mec","kinds"]).size().sort_values(ascending=False).to_string())
