import sys, re
import numpy as np
import pandas as pd

D = sys.argv[1]
pd.set_option("display.width", 220); pd.set_option("display.max_columns", 40); pd.set_option("display.max_rows", 200)
c = pd.read_csv(f"{D}/contratacoes.csv", header=10)
u = pd.read_csv(f"{D}/unidades.csv", header=6)
j = c.merge(u, left_on="N° DO PROJETO", right_on="Num TPAF", how="left")
code = j["Código da Cozinha"]
j["kind"] = np.where(code.isna(), "sem", np.where(code.astype(str).str.startswith("CS"), "CS", np.where(code.astype(str).str.startswith("EG"), "EG", "UG")))

print("== tipo de código por UF da org (linhas)")
print(pd.crosstab(j["UF ORGANIZAÇÃO"], j["kind"]).loc[lambda t: (t["EG"] + t["UG"]) > 0])
print("\n== tipo de código x Tipo Consumidor")
print(pd.crosstab(j["kind"], j["Tipo Consumidor"]))
print("\n== tipo de código x mecanismo")
print(pd.crosstab(j["MECANISMO"], j["kind"]))

for cd in ["EG000155", "unidade gestora"]:
    s = j[j["Código da Cozinha"] == cd]
    print(f"\n== {cd}: linhas {len(s)}, orgs {s['CNPJ'].nunique()}, UFs org {s['UF ORGANIZAÇÃO'].unique().tolist()}, UFs cozinha {s['UF Consumidor'].unique().tolist()}")
    print("   municípios:", s["Municipio Consumidor"].nunique(), "| nomes consumidor:", s["Nome Consumidor"].nunique(), "| CNPJ consumidor:", s["CNPJ Consumidor"].nunique())
    print("   exemplos nomes:", s["Nome Consumidor"].drop_duplicates().head(6).tolist())

# grau CS-only vs todos
links = j.dropna(subset=["Código da Cozinha"]).drop_duplicates(["CNPJ", "Código da Cozinha"])
deg_all = j.groupby("CNPJ")["Código da Cozinha"].nunique()
deg_cs = links[links["kind"] == "CS"].groupby("CNPJ").size().reindex(deg_all.index, fill_value=0)
print("\n== orgs cujo grau muda ao tirar EG/UG:", (deg_all != deg_cs).sum(), "| orgs só com EG/UG:", ((deg_cs == 0) & (deg_all > 0)).sum())

# unidade real alternativa: CNPJ consumidor + nome
links2 = j.dropna(subset=["Código da Cozinha"]).drop_duplicates(["CNPJ", "Nome Consumidor"])
deg_nome = links2.groupby("CNPJ").size().reindex(deg_all.index, fill_value=0)
print("grau por código vs por nome do consumidor — orgs com diferença:", (deg_all != deg_nome).sum(),
      "| soma graus código", deg_all.sum(), "vs nome", deg_nome.sum())
print(pd.DataFrame({"cod": deg_all, "nome": deg_nome})[deg_all != deg_nome].assign(uf=c.groupby("CNPJ")["UF ORGANIZAÇÃO"].first()).sort_values("nome", ascending=False).head(10))

# densidade por UF (só ligações dentro da UF da org, cozinhas CS)
uf_org = c.groupby("CNPJ")["UF ORGANIZAÇÃO"].first()
L = links[links["kind"] == "CS"].copy()
L = L[L["UF ORGANIZAÇÃO"] == L["UF Consumidor"]]
dens = L.groupby("UF ORGANIZAÇÃO").agg(lig=("CNPJ", "size"), orgs=("CNPJ", "nunique"), coz=("Código da Cozinha", "nunique"))
dens["densidade"] = (dens["lig"] / (dens["orgs"] * dens["coz"])).round(2)
dens["orgs_total_UF"] = uf_org.value_counts().reindex(dens.index)
print("\n== densidade bipartida por UF (ligações / orgs×cozinhas)")
print(dens.sort_values("densidade", ascending=False))

# complementaridade de produto: numa cozinha com >=2 orgs, os produtos das orgs são diferentes?
def items(s):
    if pd.isna(s): return frozenset()
    parts = re.split(r"[,|/;]| E ", str(s).upper())
    return frozenset(p.strip() for p in parts if p.strip())
prod_org = c.groupby("CNPJ")["PRODUTOS PREVISTOS NOS PROJETOS"].agg(lambda s: frozenset().union(*[items(x) for x in s]))
L["prod"] = L["CNPJ"].map(prod_org)
def overlap(df):
    ps = list(df["prod"])
    if len(ps) < 2: return np.nan
    jac = []
    for a in range(len(ps)):
        for b in range(a + 1, len(ps)):
            un = ps[a] | ps[b]
            if un: jac.append(len(ps[a] & ps[b]) / len(un))
    return np.mean(jac) if jac else np.nan
obs = L.groupby("Código da Cozinha").apply(overlap, include_groups=False).dropna()
rng = np.random.default_rng(0)
null = []
for _ in range(300):
    Ls = L.copy()
    # embaralha produtos entre orgs da mesma UF (mantém estrutura da rede e composição de produtos da UF)
    m = {}
    for uf, g in uf_org.groupby(uf_org):
        orgs = g.index.tolist(); perm = rng.permutation(orgs)
        m.update(dict(zip(orgs, perm)))
    Ls["prod"] = Ls["CNPJ"].map(lambda x: prod_org[m[x]])
    null.append(Ls.groupby("Código da Cozinha").apply(overlap, include_groups=False).dropna().mean())
null = np.array(null)
print(f"\n== sobreposição média de produtos entre fornecedores da mesma cozinha (Jaccard): obs={obs.mean():.3f}  nulo(UF)={null.mean():.3f}±{null.std():.3f}  p(nulo<=obs)={(null <= obs.mean()).mean():.3f}  n_cozinhas={len(obs)}")

# amplitude de produto vs grau (especialista vs generalista), dentro de UF
org = pd.DataFrame({"deg": deg_cs, "uf": uf_org, "n_prod": prod_org.map(len)})
org = org[org["deg"] > 0]
r_all = org["deg"].rank().corr(org["n_prod"].rank())
org["deg_c"] = org["deg"] - org.groupby("uf")["deg"].transform("mean")
org["np_c"] = org["n_prod"] - org.groupby("uf")["n_prod"].transform("mean")
print(f"== amplitude de produtos x grau: Spearman geral={r_all:.3f} | Pearson dentro de UF={org['deg_c'].corr(org['np_c']):.3f}")

# projeto: previsto vs real e valor por UR por regime
c["n_ur_prev"] = pd.to_numeric(c["Nº. DE ATENDIMENTO ÀS UNIDADES RECEBEDORAS PREVISTO*"].astype(str).str.replace(".", "", regex=False), errors="coerce")
c["valor"] = pd.to_numeric(c["VALOR TOTAL PREVISTO(R$)"].astype(str).str.replace(".", "", regex=False).str.replace(",", ".", regex=False), errors="coerce")
c["n_forn"] = pd.to_numeric(c["Nº.  FORNECEDORES PREVISTO*"], errors="coerce")
c["v_por_forn"] = c["valor"] / c["n_forn"]
print("\n== valor por agricultor fornecedor (R$) por projeto: quantis", c["v_por_forn"].quantile([.1, .25, .5, .75, .9]).round(0).to_dict())
c["deg"] = c["N° DO PROJETO"].map(u.groupby("Num TPAF")["Código da Cozinha"].nunique()).fillna(0)
c["regime"] = pd.cut(c["deg"], [-1, 0, 1, 5, 100], labels=["0", "1", "2-5", "6+"])
print(c.groupby("regime", observed=True).agg(n=("deg", "size"), valor_med=("valor", "median"), n_forn_med=("n_forn", "median"), v_por_forn_med=("v_por_forn", "median")).round(0))
print("\nvalor por projeto: % com valor 'redondo' (múltiplo de 1000):", round((c["valor"] % 1000 == 0).mean(), 3))
print("teto aparente: projetos com v_por_forn entre 14.5k e 15.0k:", ((c["v_por_forn"] > 14500) & (c["v_por_forn"] <= 15000)).sum(), "de", c["v_por_forn"].notna().sum())
print(c["v_por_forn"].round(-2).value_counts().head(8).to_dict())
