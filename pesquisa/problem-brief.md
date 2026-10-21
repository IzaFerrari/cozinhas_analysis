# Problem brief — cozinhas-por-organizacao

Construct: heterogeneidade (concentração) do nº de unidades recebedoras atendidas por organização fornecedora. É a premissa de que "quantas cozinhas cada organização atende" não tem uma resposta única e exige descrever uma distribuição, não uma média.
Population: organizações fornecedoras (CNPJ) com projeto PAA–Cozinhas em 2025 na planilha da CONAB, snapshot DATA1 de 2026-10-14 (D-4): 240 organizações e 280 projetos.
Measure: nº de `Código da Cozinha` distintos nos projetos de cada CNPJ (D-3), com três variantes de sensibilidade.
Reference: média − mediana ≥ 1 e participação dos 10% maiores ≥ 0,20 dos vínculos; fixed in D-5 (referência informada pelos dados, declarada lá). <!-- rm:ignore: limiares fixados em D-5, não são resultados -->
Basis: local — `pesquisa/agregados/problema.csv` (gerado por `pesquisa/scripts/problema.py` sobre `pesquisa/dados/brutos/`)
Magnitude: na medida principal, a média é 3,08 contra mediana 1 (diferença 2,08), e as 24 organizações do topo (10%) reúnem 0,412 dos 740 vínculos. A proporção de organizações com exatamente uma unidade é 0,458; o máximo é 23. É uma descrição censitária do snapshot, sem incerteza amostral; a principal incerteza é de medida (D-3).
Falsification: tentei fazer a heterogeneidade desaparecer de quatro formas:
- só projetos CDS, tirando os zeros de CDAF/CI: 207 organizações, média 3,41 contra mediana 2, top 10% com 0,397. A referência continua atendida.
- contando por nome normalizado (teto): média 4,30 contra mediana 2, top 10% com 0,482 de 1031 vínculos. Continua atendida, e a concentração aumenta.
- só códigos CS (sem EG e sem "unidade gestora"): média 2,92 contra mediana 1, top 10% com 0,432 de 702 vínculos. Continua atendida.
- cobertura: 0,921 dos projetos têm ao menos uma unidade registrada, então a distribuição não é produto de uma aba de unidades quase vazia.
A premissa não desaparece em nenhuma variante. O que muda entre medidas é a forma da distribuição (mediana 1 ou 2, máximo 23 ou 85), e isso é objeto da pesquisa, não refutação da premissa.
Verdict: SHOWN — a referência de D-5 vale nas quatro medidas. Ressalva: a referência é informada pelos dados, e a premissa é sobre registros (códigos), não sobre cozinhas físicas (D-3).
