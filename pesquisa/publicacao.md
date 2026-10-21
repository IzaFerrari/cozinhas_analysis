# Publicação — PUBLISH preflight (fase 8)

Data: 2026-10-21. Alvo: o manuscrito de trabalho `pesquisa/texto/artigo.md` (commit f0a8c93), com os resultados exploratórios de 2025 e o teste de H1 registrado em `BLOCKED`. **Nada foi publicado nem enviado para fora do repositório.**

## Requisitos verificáveis aqui

| Requisito | Estado | Evidência |
|---|---|---|
| Linhagem completa das afirmações materiais | atendido | validador `lineage` PASS: 8 afirmações (C1–C8) até R3/R6, RUN-3 e RUN-6 |
| Números com agregado | atendido | validador `numbers` PASS (103 números, 7 agregados) |
| Revisão adversarial separada e atual | atendido | REVIEW-3 PASS (9f123f4) + REVIEW-4 PASS (diff até 8a246a2); depois disso, só os ajustes triviais da D-19 |
| Nenhum FAIL material em aberto | atendido | REVIEW-1 e REVIEW-2 respondidas (`.research/reviews/*-respostas.md`) |
| Regeneração computacional | atendido | RUN-5 e RUN-6 com replay da ferramenta EXACT; RUN-2 a RUN-4 EXACT pelo replay manual (D-14) |
| NOT_VERIFIED materiais declarados | atendido | lista abaixo, repetida no §7 do manuscrito |

## NOT_VERIFIED declarados

- `disclosure`: não há piso de revelação. As contagens são de pessoas jurídicas de fonte pública (relatório de dados).
- `citations`: 6 de 8 alvos resolvem online; os dois PDFs do gov.br recusam o validador, e as cópias lidas estão no repositório com hash.
- Versão de 2024 do Manual de Operações da CONAB: não lida.
- Resolução PAA/GG nº 7/2023 e literatura acadêmica: só resumo.
- Licença de reuso da planilha da CONAB: não verificada.
- Exposições fora do git: não verificáveis (D-2).

## Decisões humanas pendentes (bloqueiam a publicação)

| Decisão | Por que é humana | Estado |
|---|---|---|
| Se e como publicar um trabalho cuja hipótese principal está `BLOCKED` (por exemplo, como relato exploratório com teste registrado, ou só depois de obter DATA2) | escolha de quem conduz a pesquisa | pendente |
| Venue (revista, congresso, TCC/dissertação) e as suas normas de submissão, de relato e de declaração de IA | escolha institucional e da autoria | pendente |
| Autoria e orientação | autoria | pendente |
| Licença do texto, do código e dos agregados; se as cópias brutas da planilha da CONAB podem ser redistribuídas | jurídica e institucional | pendente; licença da fonte não verificada |
| Necessidade de apreciação ética (CEP) | institucional. Os dados são administrativos públicos sobre pessoas jurídicas, sem colunas pessoais usadas, mas a decisão não é do assistente | pendente |
| Registro externo do teste de H1 (OSF ou outro) antes de abrir DATA2 | publicaria o protocolo fora do repositório | pendente (D-10) |
| DATA2: esperar que a planilha única da CONAB ganhe linhas de outro ano (D-21) | depende da CONAB | pendente (D-11, D-21) |

## Estado

Gate 8 = `blocked`, pelas decisões humanas acima. Para a pesquisa explicativa terminar com H1 em estado decidido, falta também DATA2. Quando ele existir, a sequência é:
1. commitar `pesquisa/dados/DATA2.sha256` antes de abrir o arquivo;
2. fazer o execution freeze;
3. rodar `pesquisa/scripts/h1_confirmatorio.py <DATA2> pesquisa/dados/brutos <saída> <ano>`;
4. commitar a saída e escrever o recibo confirmatório (`analysis_role: primary`, `registration`, `protocol_freeze`, `analysis_plan_freeze`, `execution_freeze`);
5. atualizar o manuscrito e pedir nova revisão.
