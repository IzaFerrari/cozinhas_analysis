# Teste do código congelado de H1 (D-17, REVIEW-2 N14) com dados sintéticos derivados de DATA1.
# Não é execução de pesquisa: não produz resultado de H1. Uso: teste_h1_sintetico.py <raiz do repositório>
import sys, os, json, shutil, tempfile, hashlib, importlib.util

raiz = os.path.abspath(sys.argv[1])
spec = importlib.util.spec_from_file_location("h1", f"{raiz}/pesquisa/scripts/h1_confirmatorio.py")
h1 = importlib.util.module_from_spec(spec); spec.loader.exec_module(h1)
brutos = f"{raiz}/pesquisa/dados/brutos"
ok = []

def caso(nome, cond):
    assert cond, nome
    ok.append(nome)

# 1. faixa e regra de decisão, com tabelas construídas
caso("borda 2,00 é pool", h1.lado_faixa(2.00) == "pool")
caso("borda 1,45 é esparsa", h1.lado_faixa(1.45) == "esparsa")
caso("1,725 é indeterminado", h1.lado_faixa(1.725) == "faixa")
r1 = {"AL": 3.0, "PB": 4.33, "RN": 2.0, "BA": 1.29, "SE": 1.33, "PR": 2.4}
def tab(razao, pool):
    return {uf: dict(razao=razao[uf], pool=pool[uf]) for uf in razao}
t = tab({"AL": 1.40, "PB": 1.30, "RN": 1.80, "BA": 2.10, "SE": 1.30, "PR": 2.50},
        {"AL": 1.0, "PB": 0.1, "RN": 0.0, "BA": 0.0, "SE": 0.0, "PR": 0.0})
d = h1.decidir(t, list(r1), razao1=r1)
caso("só contam AL, PB e BA (RN na faixa, PR herdado, SE sem mudança)", sorted(x["uf"] for x in d["ufs"]) == ["AL", "BA", "PB"])
caso("2 de 3 para a regra dá INCONCLUSIVE", d["estado"] == "INCONCLUSIVE" and d["acertos_regra"] == 2)
t["PB"]["pool"] = 1.0
caso("3 de 3 para a regra dá CONFIRMED", h1.decidir(t, list(r1), razao1=r1)["estado"] == "CONFIRMED")
for uf in ["AL", "PB"]: t[uf]["pool"] = 0.0
t["BA"]["pool"] = 1.0
caso("3 de 3 para a escassez dá REFUTED", h1.decidir(t, list(r1), razao1=r1)["estado"] == "REFUTED")
caso("ponto 1,725 conta RN em 1,70", any(x["uf"] == "RN" for x in h1.decidir(
    tab({"RN": 1.70}, {"RN": 1.0}), ["RN"], h1.lado_ponto(1.725), razao1={"RN": 2.0})["ufs"]))

# 2. integração com DATA2 sintético (DATA1 com ANO e nº de projeto trocados para 2026)
def sintetico(pasta, troca=lambda s: s):
    os.makedirs(pasta)
    for n in ["contratacoes.csv", "unidades.csv"]:
        linhas = open(f"{brutos}/{n}", encoding="utf-8").read().split("\n")
        novas = [troca(("2026," + l[5:]).replace("/2025/", "/2026/")) if l.startswith("2025,") else troca(l) for l in linhas]
        open(f"{pasta}/{n}", "w", encoding="utf-8").write("\n".join(novas))

def rodar(pasta, ano, com_hash=True):
    cwd = tempfile.mkdtemp()
    os.makedirs(f"{cwd}/pesquisa/dados")
    if com_hash:
        with open(f"{cwd}/pesquisa/dados/DATA2.sha256", "w") as f:
            for n in ["contratacoes.csv", "unidades.csv"]:
                f.write(hashlib.sha256(open(f"{pasta}/{n}", "rb").read()).hexdigest() + "  " + n + "\n")
    antes = os.getcwd(); os.chdir(cwd)
    try:
        h1.main(pasta, brutos, f"{cwd}/saida.json", ano)
        return json.load(open(f"{cwd}/saida.json"))
    except SystemExit as e:
        return str(e)
    finally:
        os.chdir(antes); shutil.rmtree(cwd)

base = tempfile.mkdtemp()
igual = f"{base}/igual"; sintetico(igual)
r = rodar(igual, "2026")
caso("2026: PI exposto e excluído", isinstance(r, dict) and r["expostas_excluidas"] == ["PI"])
caso("2026: PR herdado, fora de K2", list(r["herdadas_relato"]) == ["PR"] and "PR" not in r["utilizaveis_K2"])
caso("2026: seis utilizáveis, nenhum discordante, INCONCLUSIVE", len(r["utilizaveis_K2"]) == 6 and r["T1"]["discordantes"] == 0 and r["T1"]["estado"] == "INCONCLUSIVE")
caso("2026: nenhum projeto repetido de DATA1", r["projetos_ja_em_data1"] == 0)
caso("sem arquivo de hash: BLOCKED", "BLOCKED" in rodar(igual, "2026", com_hash=False))
rotulo = f"{base}/rotulo"; sintetico(rotulo, lambda s: s.replace(",CDS,", ",CDSX,"))
caso("rótulo de mecanismo estranho: BLOCKED (K1)", "BLOCKED (K1)" in rodar(rotulo, "2026"))
semano = f"{base}/semano"; sintetico(semano, lambda s: s.replace("ANO,", "ANNO,", 1) if s.startswith("ANO,") else s)
caso("sem coluna ANO: BLOCKED (K1)", "BLOCKED (K1)" in rodar(semano, "2026"))
repetido = f"{base}/repetido"; os.makedirs(repetido)
for n in ["contratacoes.csv", "unidades.csv"]:
    shutil.copy(f"{brutos}/{n}", f"{repetido}/{n}")
caso("só projetos já vistos (ano 2025, não ensaio): BLOCKED", "BLOCKED" in rodar(repetido, "2025"))
shutil.rmtree(base)
print(f"{len(ok)} casos passaram:")
print("\n".join(f"- {c}" for c in ok))
