# H2 (analysis-plan.md, modo exploratório): elasticidade do grau em relação ao kg previsto, em DATA1;
# mais a distribuição do grau e a perda previsto→registrado por faixa de tamanho (descrição).
# Uso: h2_exploratorio.py <brutos> <saida.json>
import sys, json, hashlib
import numpy as np, pandas as pd
from scipy import stats

base, saida = sys.argv[1], sys.argv[2]
SHA = {"contratacoes.csv": "480b46c4660add2d8f8f64b1206bd04c05a85e21432b4cc5b9103879ebd31dbc",
       "unidades.csv": "6754d7152e46ded005c27e61072420b40710a80bec86be79b3184fd0bc1db102"}
for nome, h in SHA.items():  # DATA1 (D-1)
    assert hashlib.sha256(open(f"{base}/{nome}", "rb").read()).hexdigest() == h, nome

c = pd.read_csv(f"{base}/contratacoes.csv", header=10, dtype=str)
u = pd.read_csv(f"{base}/unidades.csv", header=6, dtype=str)
u["cod"] = u["Código da Cozinha"].str.strip()
def num(s):
    s = s.fillna("").str.strip().str.replace(".", "", regex=False).str.replace(",", ".", regex=False)
    return pd.to_numeric(s.replace({"-": None, "": None}), errors="coerce")
cds = c[c["MECANISMO RESUMO 2"] == "CDS"].copy()
cds["kg"] = num(cds["QUANTIDADE PREVISTA (KG)"])
cds["prev"] = pd.to_numeric(cds["Nº. DE ATENDIMENTO ÀS UNIDADES RECEBEDORAS PREVISTO*"], errors="coerce")
cds["reg"] = cds["N° DO PROJETO"].map(u.groupby("Num TPAF")["cod"].nunique()).fillna(0)
v = (cds[["N° DO PROJETO", "CNPJ"]].merge(u[["Num TPAF", "cod"]], left_on="N° DO PROJETO", right_on="Num TPAF")
     .drop_duplicates(["CNPJ", "cod"]))
org = cds.groupby("CNPJ").agg(uf=("UF ORGANIZAÇÃO", "first"), kg=("kg", "sum"), prev=("prev", "sum"))
org["grau"] = v.groupby("CNPJ")["cod"].nunique().reindex(org.index).fillna(0)
out = {}

# descrição: distribuição do grau (organizações CDS com >= 1 unidade)
g = org.loc[org["grau"] > 0, "grau"]
out["grau"] = dict(organizacoes=int(len(g)), vinculos=int(g.sum()), mediana=float(g.median()),
                   media=round(float(g.mean()), 2), p90=float(g.quantile(0.9)), maximo=int(g.max()),
                   prop_grau1=round(float((g == 1).mean()), 3))

# descrição: perda previsto→registrado por faixa do previsto (projetos CDS)
faixas = pd.cut(cds["prev"], [0, 1, 3, 9, 999], labels=["1", "2-3", "4-9", "10+"])
f = cds.groupby(faixas, observed=True).agg(projetos=("prev", "size"), com_perda=("reg", lambda s: int((s < cds.loc[s.index, "prev"]).sum())),
                                           previsto=("prev", "sum"), registrado=("reg", "sum"))
f["perda"] = (1 - f["registrado"] / f["previsto"]).round(3)
out["perda_por_faixa"] = {k: {kk: (float(vv) if kk == "perda" else int(vv)) for kk, vv in r.items()} for k, r in f.iterrows()}
out["perda_total"] = round(float(1 - cds["reg"].sum() / cds["prev"].sum()), 3)
out["registrado_acima_previsto"] = int((cds["reg"] > cds["prev"]).sum())

# T6: elasticidade dentro da UF, erro-padrão agrupado por UF (CR1), IC t com G-1 graus de liberdade
def elasticidade(y):
    d = org[(org["grau"] > 0) & (org["kg"] > 0) & org[y].gt(0)].copy()
    d["ly"], d["lx"] = np.log(d[y]), np.log(d["kg"])
    d = d[d.groupby("uf")["uf"].transform("size") >= 2]  # efeito fixo de UF exige >= 2 organizações
    for col in ["ly", "lx"]:
        d[col + "_c"] = d[col] - d.groupby("uf")[col].transform("mean")
    x, yv = d["lx_c"].to_numpy(), d["ly_c"].to_numpy()
    beta = float((x @ yv) / (x @ x))
    e = yv - beta * x
    n, G, k = len(d), d["uf"].nunique(), 1 + d["uf"].nunique()
    scores = d.assign(s=x * e).groupby("uf")["s"].sum().to_numpy()
    var = (G / (G - 1)) * ((n - 1) / (n - k)) * float(scores @ scores) / float(x @ x) ** 2
    se = var ** 0.5
    t = stats.t.ppf(0.975, G - 1)
    return dict(beta=round(beta, 3), ep=round(se, 3), ic95=[round(beta - t * se, 3), round(beta + t * se, 3)],
                organizacoes=n, ufs=G)
out["T6_grau_registrado"] = elasticidade("grau")
out["T7_grau_previsto"] = elasticidade("prev")
with open(saida, "w") as fh:
    json.dump(out, fh, ensure_ascii=False, indent=1, sort_keys=True)
