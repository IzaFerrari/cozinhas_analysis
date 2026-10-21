# Checagem só estrutural do arquivo-fonte atual (D-11, D-15): nomes das abas, valores distintos de ANO
# e nº de linhas não vazias em ANO. Não lê desfechos. Uso: checa_fonte.py <xlsx> <saida.json>
import sys, json, zipfile, re, hashlib
import pandas as pd
f, saida = sys.argv[1], sys.argv[2]
abas = re.findall(r'<sheet [^>]*name="([^"]+)"', zipfile.ZipFile(f).read("xl/workbook.xml").decode())
out = dict(sha256=hashlib.sha256(open(f, "rb").read()).hexdigest(), abas=abas)
for aba, h in [("CONTRATAÇÕES 2025", 10), ("UNIDADES RECEBEDORAS", 6)]:
    d = pd.read_excel(f, sheet_name=aba, header=h, usecols=["ANO"], dtype=str).dropna()
    out[aba] = dict(anos=sorted(d["ANO"].str.strip().unique()), linhas=len(d))
json.dump(out, open(saida, "w"), ensure_ascii=False, indent=1)
