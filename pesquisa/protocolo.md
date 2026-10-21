# Protocolo — Cozinhas Solidárias: unidades recebedoras por organização fornecedora (PAA 2025)

Estado: rascunho (fase 1). Ainda não congelado. O congelamento acontece na fase 3.

## Question

Quantas unidades recebedoras do Programa Cozinha Solidária cada organização fornecedora contratada pela CONAB no PAA em 2025 atende, e como esse número se distribui entre as organizações?

Claim: descriptive
Unit of analysis: organização fornecedora, identificada pelo CNPJ, com pelo menos um projeto PAA–Cozinhas de 2025 na planilha da CONAB (DATA1, D-4).
Estimand: para todas as organizações fornecedoras do snapshot DATA1 (população censitária, não amostra), a distribuição do nº de unidades recebedoras distintas (`Código da Cozinha`, D-3) vinculadas aos projetos de 2025 de cada organização. Resumos: mediana e quartis, proporção de organizações com 0, 1, 2–9 e 10 ou mais unidades, máximo, e participação dos 10% maiores no total de vínculos organização–unidade. Estratificado por mecanismo (CDS vs CDAF/CI) e por UF da organização.
Refutation: a pergunta fica errada ou bem mais estreita se (a) o `Código da Cozinha` não identifica unidades recebedoras de forma consistente, e então a contagem deixa de medir "unidades atendidas" e passa a medir "registros"; (b) a aba de unidades não for um registro completo, de modo que os projetos sem unidade sejam lacunas de cadastro e não zeros reais; ou (c) o snapshot mudar materialmente antes da análise final (a fonte é alterável).
Objection: a objeção mais forte é de medida. A granularidade do código varia: há códigos `EG…` que reúnem várias cozinhas, códigos `CS…` com dezenas de nomes de consumidor e o registro "unidade gestora" (CONAB, SESC, CEAGESP) atuando como intermediário. Ela será tratada na fase 4 (relatório de dados), reportando lado a lado as medidas de D-3 (código, nome normalizado, só CS, só CDS). O significado do código fica em aberto por decisão humana (D-3), e o texto falará em "unidades recebedoras registradas".
Who cares: trabalho acadêmico de quem conduz a pesquisa (IzaFerrari). A consequência é de conhecimento: caracterizar como os fornecedores do PAA se ligam às cozinhas solidárias em 2025 e mostrar quanto a resposta depende da unidade de contagem.
Non-goals: não explica por que a distribuição tem essa forma (as linhagens explicativas estão em `Deferred`, D-2); não faz inferência causal; não avalia desempenho do programa, volume entregue, valor ou pessoas atendidas; não cobre outros anos nem outras modalidades além das da planilha; não testa hipóteses confirmatórias com DATA1 (D-4).

## Portfólio ativo

Componentes descritivos adotados da exploração (`pesquisa/exploracao/2026-10-14-explorer.md`), todos dentro do escopo de D-2:

1. Distribuição nacional pela medida principal (código distinto).
2. Sensibilidade à unidade de contagem: nome normalizado (teto), só códigos CS e só projetos CDS (linhagem 1 da exploração).
3. Estratificação por mecanismo e UF, incluindo a decomposição contábil grau médio = (unidades ÷ organizações) × (organizações por unidade), como descrição e não como explicação (linhagens 2 e 4).

Nenhuma hipótese confirmatória é formulada sobre DATA1 (D-4).
