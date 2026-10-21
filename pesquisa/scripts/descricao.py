# Descrição censitária da estrutura organização–unidade por UF em DATA1 (H3, exploratório; D-23).
# Uso: descricao.py <brutos> <saida.json>
import sys, json, hashlib
import pandas as pd

base, saida = sys.argv[1], sys.argv[2]
SHA = {"contratacoes.csv": "480b46c4660add2d8f8f64b1206bd04c05a85e21432b4cc5b9103879ebd31dbc",
       "unidades.csv": "6754d7152e46ded005c27e61072420b40710a80bec86be79b3184fd0bc1db102"}
for nome, h in SHA.items():  # DATA1 (D-1)
    assert hashlib.sha256(open(f"{base}/{nome}", "rb").read()).hexdigest() == h, nome
c = pd.read_csv(f"{base}/contratacoes.csv", header=10, dtype=str)
u = pd.read_csv(f"{base}/unidades.csv", header=6, dtype=str)
c["CNPJ"] = c["CNPJ"].str.replace(r"\D", "", regex=True)
u["cod"] = u["Código da Cozinha"].str.strip().str.upper()
cds = c[c["MECANISMO RESUMO 2"].str.strip() == "CDS"]
v = (cds[["N° DO PROJETO", "CNPJ", "UF ORGANIZAÇÃO"]].merge(u[["Num TPAF", "cod"]], left_on="N° DO PROJETO", right_on="Num TPAF"))
v = v[v["cod"].str.fullmatch(r"(CS|EG)\d+")].drop_duplicates(["CNPJ", "cod"])  # regra de código da D-16


def componentes(d):
    pai = {}
    def raiz(x):
        while pai.setdefault(x, x) != x:
            pai[x] = pai[pai[x]]; x = pai[x]
        return x
    for o, k in zip(d["CNPJ"], d["cod"]):
        pai[raiz(("o", o))] = raiz(("u", k))
    d = d.assign(comp=[raiz(("o", o)) for o in d["CNPJ"]])
    r = d.groupby("comp").agg(orgs=("CNPJ", "nunique"), unid=("cod", "nunique"), vinc=("cod", "size"))
    r["dens"] = r["vinc"] / (r["orgs"] * r["unid"])
    return r


out = {"por_uf": {}}
for uf, d in v.groupby("UF ORGANIZAÇÃO"):
    n_o, n_u, n_v = d["CNPJ"].nunique(), d["cod"].nunique(), len(d)
    if n_u < 10 or n_o < 3:
        continue
    r = componentes(d)
    maior = r.sort_values("vinc").iloc[-1]
    por_unid = d.groupby("cod")["CNPJ"].nunique()
    out["por_uf"][uf] = dict(
        organizacoes=n_o, unidades=n_u, vinculos=n_v,
        unidades_por_organizacao=round(n_u / n_o, 4),
        vinculos_por_organizacao=round(n_v / n_o, 4),
        organizacoes_por_unidade_media=round(n_v / n_u, 4),
        organizacoes_por_unidade_mediana=float(por_unid.median()),
        fracao_unidades_2mais=round(float((por_unid >= 2).mean()), 4),
        cobertura_media=round(n_v / (n_o * n_u), 4),  # fração das unidades da UF atendida por organização, em média
        componentes=len(r),
        maior_componente_organizacoes=int(maior["orgs"]), maior_componente_unidades=int(maior["unid"]),
        maior_componente_densidade=round(float(maior["dens"]), 4),
        fracao_vinculos_maior_componente=round(float(maior["vinc"] / n_v), 4),
        participacao_pool=round(float(r[(r["orgs"] >= 2) & (r["dens"] >= 0.5)]["vinc"].sum() / n_v), 4),
        fracao_exclusiva=round(float(r[r["orgs"] == 1]["vinc"].sum() / n_v), 4),
    )
t = pd.DataFrame(out["por_uf"]).T.astype(float)
out["ufs"] = sorted(out["por_uf"])
out["spearman_pool_organizacoes"] = round(float(t["participacao_pool"].corr(t["organizacoes"], method="spearman")), 3)
out["spearman_pool_razao"] = round(float(t["participacao_pool"].corr(t["unidades_por_organizacao"], method="spearman")), 3)
out["spearman_pool_cobertura"] = round(float(t["participacao_pool"].corr(t["cobertura_media"], method="spearman")), 3)
out["faixas"] = {k: [round(float(t[k].min()), 4), round(float(t[k].max()), 4)]
                 for k in ["vinculos_por_organizacao", "organizacoes_por_unidade_media", "cobertura_media"]}
with open(saida, "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=1, sort_keys=True)
