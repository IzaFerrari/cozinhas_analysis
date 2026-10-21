import sys, re, unicodedata, numpy as np, pandas as pd
D=sys.argv[1]; pd.set_option("display.width",220)
c=pd.read_csv(f"{D}/contratacoes.csv",header=10); u=pd.read_csv(f"{D}/unidades.csv",header=6)
def norm(x):
    x=unicodedata.normalize("NFKD",str(x)).encode("ascii","ignore").decode().upper()
    x=re.sub(r"[^A-Z0-9 ]"," ",x); x=re.sub(r"\b(DA|DE|DO|DAS|DOS|E)\b"," ",x); return re.sub(r"\s+"," ",x).strip()
j=c.merge(u,left_on="N° DO PROJETO",right_on="Num TPAF",how="left"); j["nn"]=j["Nome Consumidor"].map(norm)
L=j.dropna(subset=["Código da Cozinha"])
dc=j.groupby("CNPJ")["Código da Cozinha"].nunique(); dn=L.groupby("CNPJ")["nn"].nunique().reindex(dc.index,fill_value=0)
uf=c.groupby("CNPJ")["UF ORGANIZAÇÃO"].first()
o=pd.DataFrame({"code":dc,"nome":dn,"uf":uf})
t=o.groupby("uf").agg(n=("code","size"),med_code=("code","median"),mean_code=("code","mean"),med_nome=("nome","median"),mean_nome=("nome","mean")).round(1)
t["rank_code"]=t.mean_code.rank(ascending=False).astype(int); t["rank_nome"]=t.mean_nome.rank(ascending=False).astype(int)
print(t.sort_values("mean_nome",ascending=False).head(10))
for col in ["code","nome"]:
    gm=o[col].mean(); print(col,"eta2 UF:",round(((o.groupby("uf")[col].transform("mean")-gm)**2).sum()/((o[col]-gm)**2).sum(),3),
          "| top10% share:", round(o[col].sort_values(ascending=False).head(24).sum()/o[col].sum(),3))
