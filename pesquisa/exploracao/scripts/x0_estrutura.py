# Exploração 2026-10-21 (D-4), DATA1, papel discovery. Estrutura das colunas.
import sys, pandas as pd
base = sys.argv[1]
c = pd.read_csv(f"{base}/contratacoes.csv", header=10, dtype=str)
u = pd.read_csv(f"{base}/unidades.csv", header=6, dtype=str)
print(c.shape, u.shape)
for col in ["MECANISMO", "MECANISMO RESUMO 1", "MECANISMO RESUMO 2", "RECURSO", "TIPO ORGANIZAÇÃO", "Tipo de Organização Declarada"]:
    print("\n##", col); print(c[col].value_counts(dropna=False).head(12).to_string())
print("\n## PRODUTOS (amostra)"); print(c.iloc[:, 29].value_counts().head(15).to_string())
print("\n## colunas c:", list(c.columns))
for col in ["MODALIDADE 1", "Tipo Consumidor", "Tipo Consumidor RESUMO", "Ind CNPJ Proprio"]:
    print("\n##", col); print(u[col].value_counts(dropna=False).head(12).to_string())
print("\n## segmento do nº do projeto"); print(c["N° DO PROJETO"].str.split("/").str[2].value_counts().to_string())
print("\n## unidades previstas (amostra)"); print(c.iloc[:, 16].value_counts().head(10).to_string())
