# H1 (analysis-plan.md): o regime de alocação da UF persiste ou segue a escassez?
# Uso: h1_confirmatorio.py <alvo> <referencia> <saida.json> <ano> <sha_contratacoes> <sha_unidades>
#   alvo        pasta com contratacoes.csv e unidades.csv do ano confirmatório (DATA2)
#   referencia  pasta com o DATA1 (classes, K5/T2, T5 e exclusão de projetos já vistos)
#   ano         ano confirmatório; só linhas com ANO igual entram. "2025-ensaio" = ensaio em amostra
#               com DATA1 como alvo (sem exclusão de projetos já vistos); nunca é teste de H1
#   sha_*       hashes de DATA2 registrados em decisoes.md antes de abrir; divergência para a execução
# Congelado com o plano (D-10, D-12, D-16). Mudança depois do congelamento só por CHANGE_PLAN.
import sys, json, hashlib
from math import comb
import pandas as pd

# Compromissos fixados no plano (D-9), a partir de pesquisa/agregados/problema.csv (DATA1)
CLASSE_DATA1 = {"AL": "pool", "PB": "pool", "PE": "pool", "RN": "pool", "SC": "pool",
                "BA": "esparsa", "MG": "esparsa", "PI": "esparsa", "PR": "esparsa", "RS": "esparsa", "SE": "esparsa"}
LIMIAR_POOL = 0.5          # classe pool se participação de pool >= 0,5
LIMIAR_ESCASSEZ = 1.725    # razão unidades/organizações; ponto médio de (1,45; 2,00]
LIMIARES_T4 = [1.60, 1.85]
MIN_UNIDADES, MIN_ORGS = 10, 3
MAX_PERDA = 0.3            # K3 (DATA2) e K7 (DATA1, D-12): UF com perda previsto→registrado acima disso sai da contagem
EXCLUIDAS_K7 = ["MG", "PE", "RS"]  # perda em DATA1 > 0,3 (RUN-1)
MIN_DISCORDANTES, PROP_DECISAO = 3, 0.75
MIN_UFS = 6                # K2
BANDA_T3 = (0.4, 0.6)
MIN_VINC_T2 = 5
CODIGO_UNIDADE = r"(CS|EG)\d+"          # D-16: marcadores como "unidade gestora" não são unidades
MECANISMOS = {"CDS", "CDAF", "CI"}       # D-16: K1 confere o conjunto de rótulos
EXPOSTAS = {"2026": ["PI"]}              # D-16: UF cuja razão do ano confirmatório foi vista antes do congelamento
COLUNAS_C = ["N° DO PROJETO", "CNPJ", "UF ORGANIZAÇÃO", "MECANISMO RESUMO 2", "Nº. DE ATENDIMENTO ÀS UNIDADES RECEBEDORAS PREVISTO*"]
COLUNAS_U = ["Num TPAF", "Código da Cozinha", "UF Consumidor"]


def ler(pasta, nome, chave):
    bruto = pd.read_csv(f"{pasta}/{nome}", header=None, dtype=str, skip_blank_lines=False)
    linha = bruto.index[bruto.apply(lambda r: r.astype(str).str.strip().eq(chave).any(), axis=1)][0]
    return pd.read_csv(f"{pasta}/{nome}", header=linha, dtype=str, skip_blank_lines=False)


def carregar(pasta):
    c = ler(pasta, "contratacoes.csv", "N° DO PROJETO")
    u = ler(pasta, "unidades.csv", "Num TPAF")
    faltam = [x for x in COLUNAS_C if x not in c.columns] + [x for x in COLUNAS_U if x not in u.columns]
    if faltam:  # K1
        raise SystemExit(f"BLOCKED (K1): colunas ausentes {faltam}")
    c = c.assign(CNPJ=c["CNPJ"].str.replace(r"\D", "", regex=True))
    u = u.assign(cod=u["Código da Cozinha"].str.strip().str.upper())
    return c, u


def filtrar_ano(c, u, ano):
    return c[c["ANO"].str.strip() == ano], u[u["ANO"].str.strip() == ano]


def vinculos(c, u, so_cs=False):
    cds = c[c["MECANISMO RESUMO 2"].str.strip() == "CDS"]
    v = (cds[["N° DO PROJETO", "CNPJ", "UF ORGANIZAÇÃO"]]
         .merge(u[["Num TPAF", "cod", "UF Consumidor"]], left_on="N° DO PROJETO", right_on="Num TPAF"))
    v = v[v["cod"].notna() & v["cod"].str.fullmatch(CODIGO_UNIDADE)]
    if so_cs:
        v = v[v["cod"].str.upper().str.startswith("CS")]
    return v.drop_duplicates(["CNPJ", "cod"])


def participacao_pool(d):
    """Fração dos vínculos em componentes conexos com >= 2 organizações e densidade >= 0,5 (D-6)."""
    if d.empty:
        return float("nan")
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
    return float(r[(r["orgs"] >= 2) & (r["dens"] >= 0.5)]["vinc"].sum() / len(d))


def por_uf(v):
    linhas = {}
    for uf, d in v.groupby("UF ORGANIZAÇÃO"):
        n_o, n_u = d["CNPJ"].nunique(), d["cod"].nunique()
        linhas[uf] = dict(organizacoes=n_o, unidades=n_u, vinculos=len(d), razao=n_u / n_o,
                          pool=participacao_pool(d), interestadual=float((d["UF Consumidor"].str.strip() != uf).mean()),
                          nao_cs=float((~d["cod"].str.upper().str.startswith("CS")).mean()))
    return linhas


def perda(c, u):
    cds = c[c["MECANISMO RESUMO 2"].str.strip() == "CDS"].copy()
    cds["prev"] = pd.to_numeric(cds["Nº. DE ATENDIMENTO ÀS UNIDADES RECEBEDORAS PREVISTO*"], errors="coerce")
    cds["reg"] = cds["N° DO PROJETO"].map(u.groupby("Num TPAF")["cod"].nunique()).fillna(0)
    cds = cds[cds["prev"].notna()]
    g = cds.groupby("UF ORGANIZAÇÃO")[["prev", "reg"]].sum()
    return {uf: float(1 - min(r["reg"], r["prev"]) / r["prev"]) if r["prev"] > 0 else float("nan") for uf, r in g.iterrows()}


def classe(p):
    return "pool" if p >= LIMIAR_POOL else "esparsa"


def decidir(tab, ufs, limiar, chave_pool="pool", ref=CLASSE_DATA1, razao1=None):
    # D-16: só conta a UF cuja classe de escassez muda entre DATA1 e DATA2 (a razão cruza o limiar)
    disc = []
    for uf in ufs:
        t = tab[uf]
        escassez = "pool" if t["razao"] >= limiar else "esparsa"
        escassez1 = "pool" if razao1[uf] >= limiar else "esparsa"
        if escassez != escassez1 and escassez != ref[uf]:
            obs = classe(t[chave_pool])
            disc.append(dict(uf=uf, regra=ref[uf], escassez=escassez, observado=obs,
                             acerta=("regra" if obs == ref[uf] else "escassez")))
    n = len(disc)
    w_r = sum(d["acerta"] == "regra" for d in disc)
    w_e = n - w_r
    if n < MIN_DISCORDANTES:
        estado = "INCONCLUSIVE"
    elif w_r / n >= PROP_DECISAO:
        estado = "CONFIRMED"
    elif w_e / n >= PROP_DECISAO:
        estado = "REFUTED"
    else:
        estado = "INCONCLUSIVE"
    cauda = sum(comb(n, k) for k in range(max(w_r, w_e), n + 1)) / 2 ** n if n else None
    return dict(estado=estado, discordantes=n, acertos_regra=w_r, acertos_escassez=w_e,
                p_binomial_meio=cauda, ufs=disc)


def main(alvo, referencia, saida, ano, sha_c, sha_u):
    esperado = {"contratacoes.csv": sha_c, "unidades.csv": sha_u}
    for n, h in esperado.items():
        if hashlib.sha256(open(f"{alvo}/{n}", "rb").read()).hexdigest() != h:
            raise SystemExit(f"hash de {n} não confere com o registrado")
    c2, u2 = carregar(alvo)
    c1, u1 = carregar(referencia)
    rotulos = set(c2["MECANISMO RESUMO 2"].dropna().str.strip())
    if not rotulos <= MECANISMOS or "CDS" not in rotulos:  # K1
        raise SystemExit(f"BLOCKED (K1): rótulos de mecanismo {sorted(rotulos)}")
    ensaio = ano.endswith("-ensaio")
    ano = ano.split("-")[0]
    c2, u2 = filtrar_ano(c2, u2, ano)
    ja_vistos = set(c1["N° DO PROJETO"].str.strip())
    repetidos = int(c2["N° DO PROJETO"].str.strip().isin(ja_vistos).sum())
    if not ensaio:
        c2 = c2[~c2["N° DO PROJETO"].str.strip().isin(ja_vistos)]
    v2, v1 = vinculos(c2, u2), vinculos(c1, u1)
    if v2.empty:  # K1
        raise SystemExit("BLOCKED (K1): nenhum vínculo CDS no ano confirmatório")
    tab = por_uf(v2)
    perdas = perda(c2, u2)
    pares1 = set(zip(v1["CNPJ"], v1["cod"]))
    for uf, t in tab.items():
        d = v2[v2["UF ORGANIZAÇÃO"] == uf]
        repetido = [(o, k) in pares1 for o, k in zip(d["CNPJ"], d["cod"])]
        t["sobreposicao_data1"] = float(sum(repetido) / len(d))
        novos = d[[not r for r in repetido]]
        t["pool_novos"] = participacao_pool(novos) if len(novos) >= MIN_VINC_T2 else None
        t["perda"] = perdas.get(uf)
        t["elegivel"] = t["unidades"] >= MIN_UNIDADES and t["organizacoes"] >= MIN_ORGS

    DATA1_SHA = {"contratacoes.csv": "480b46c4660add2d8f8f64b1206bd04c05a85e21432b4cc5b9103879ebd31dbc",
                 "unidades.csv": "6754d7152e46ded005c27e61072420b40710a80bec86be79b3184fd0bc1db102"}
    ref_sha = {n: hashlib.sha256(open(f"{referencia}/{n}", "rb").read()).hexdigest() for n in DATA1_SHA}
    if ref_sha != DATA1_SHA:
        raise SystemExit("referência não é o DATA1 registrado (D-1)")
    tab1 = por_uf(v1)
    if any(classe(tab1[uf]["pool"]) != CLASSE_DATA1[uf] for uf in CLASSE_DATA1):
        raise SystemExit("constantes de CLASSE_DATA1 não batem com o recálculo sobre DATA1")
    perdas1 = perda(c1, u1)
    if sorted(uf for uf in CLASSE_DATA1 if perdas1[uf] > MAX_PERDA) != EXCLUIDAS_K7:
        raise SystemExit("K7 recalculada sobre DATA1 não bate com EXCLUIDAS_K7")
    razao1 = {uf: tab1[uf]["razao"] for uf in CLASSE_DATA1}
    # D-16: ordem fixa — elegibilidade nos dois anos → K7 → K3 → UFs expostas → K2
    elegiveis = sorted(uf for uf in CLASSE_DATA1 if uf in tab and tab[uf]["elegivel"])
    k3_fora = [uf for uf in elegiveis if uf not in EXCLUIDAS_K7 and (tab[uf]["perda"] is None or tab[uf]["perda"] > MAX_PERDA)]
    expostas = [uf for uf in EXPOSTAS.get(ano, []) if uf in elegiveis]
    primarias = [uf for uf in elegiveis if uf not in EXCLUIDAS_K7 and uf not in k3_fora and uf not in expostas]
    out_k7 = EXCLUIDAS_K7
    out = dict(ensaio=ensaio, entrada={n: hashlib.sha256(open(f"{alvo}/{n}", "rb").read()).hexdigest() for n in ["contratacoes.csv", "unidades.csv"]},
               por_uf=tab, elegiveis=elegiveis, K7_excluidas=out_k7, K3_excluidas=k3_fora,
               expostas_excluidas=expostas, primarias=primarias, projetos_ja_em_data1=repetidos,
               razao_data1=razao1)
    # relato à parte (D-16): UFs fora da primária por exposição e a discordância herdada de DATA1 (PR)
    out["expostas_relato"] = {uf: dict(razao=tab[uf]["razao"], classe=classe(tab[uf]["pool"])) for uf in expostas}
    out["herdadas_relato"] = {uf: dict(razao=tab[uf]["razao"], classe=classe(tab[uf]["pool"]))
                              for uf in primarias if (razao1[uf] >= LIMIAR_ESCASSEZ) != (CLASSE_DATA1[uf] == "pool")}
    if len(primarias) < MIN_UFS:  # K2
        out["T1"] = dict(estado="INCONCLUSIVE", motivo=f"K2: {len(primarias)} UFs utilizáveis (< {MIN_UFS})")
    else:
        out["T1"] = decidir(tab, primarias, LIMIAR_ESCASSEZ, razao1=razao1)
        out["T2"] = decidir(tab, [uf for uf in primarias if tab[uf]["pool_novos"] is not None], LIMIAR_ESCASSEZ, "pool_novos", razao1=razao1)
        out["T3"] = decidir(tab, [uf for uf in primarias if not (BANDA_T3[0] <= tab[uf]["pool"] <= BANDA_T3[1])], LIMIAR_ESCASSEZ, razao1=razao1)
        out["T4"] = {str(l): decidir(tab, primarias, l, razao1=razao1) for l in LIMIARES_T4}
        tab_cs, tab1_cs = por_uf(vinculos(c2, u2, so_cs=True)), por_uf(vinculos(c1, u1, so_cs=True))
        ufs_cs = [uf for uf in primarias if uf in tab_cs and uf in tab1_cs]
        out["T5"] = decidir(tab_cs, ufs_cs, LIMIAR_ESCASSEZ, ref={uf: classe(tab1_cs[uf]["pool"]) for uf in ufs_cs},
                            razao1={uf: tab1_cs[uf]["razao"] for uf in ufs_cs})
    out["K4_interestadual_max"] = max(tab[uf]["interestadual"] for uf in elegiveis) if elegiveis else None
    out["K5_sobreposicao_mediana_discordantes"] = (
        float(pd.Series([tab[d["uf"]]["sobreposicao_data1"] for d in out["T1"].get("ufs", [])]).median())
        if out["T1"].get("ufs") else None)
    with open(saida, "w") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, sort_keys=True)


if __name__ == "__main__":
    main(*sys.argv[1:7])
