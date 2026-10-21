# Protocolo — Por que algumas organizações fornecedoras do PAA–Cozinhas atendem muito mais unidades

Estado: congelado (fase 3, D-10). Mudança material só por bloco novo em `decisoes.md` (CHANGE_PLAN). O congelamento é o commit que traz este estado junto com `analysis-plan.md` em `Freeze: frozen`. Registro: interno, `pesquisa/registro.md` (D-10).

## Question

Por que algumas organizações fornecedoras de projetos CDS do PAA–Cozinhas da CONAB atendem muito mais unidades recebedoras do que outras? Em particular, o grau alto em AL, PB e RN vem de uma regra de montagem das propostas própria da UF (pool de unidades compartilhado) ou da escassez local de organizações em relação às unidades?

Claim: associational
Unit of analysis: a organização fornecedora (CNPJ) com projeto CDS–Cozinhas na planilha da CONAB, para o grau; e a UF, para o regime de alocação.
Estimand: em dado independente de DATA1 (D-2), há dois contrastes. (i) Entre UFs: a associação entre a forma do grafo organização–unidade (índice de compartilhamento ajustado por tamanho, a fixar na fase 3) e a razão unidades/organizações, comparada com a persistência do regime de cada UF previsto a partir de DATA1 e congelado antes de abrir o dado novo. (ii) Entre organizações, dentro do regime: a elasticidade do grau em relação à quantidade prevista (kg); na fase 3 ela passou a ser só exploratória, em DATA1 (D-9). O desfecho é o grau registrado, e a perda previsto→registrado é checagem (K3) e descrição (D-9).
Refutation: a pergunta fica errada ou bem mais estreita se (a) não houver dado independente adequado, isto é, outro ano da mesma planilha ou projetos novos (as hipóteses terminam em `BLOCKED` e o que vier de DATA1 é só exploratório, D-3); (b) documentos das chamadas mostrarem uma regra nacional única em que a organização escolhe livremente as unidades (aí "regra da UF" deixa de ser candidata e a pergunta passa a ser por que as organizações escolhem assim); (c) a diferença entre UFs sumir quando o grafo é dividido em componentes conexos, ou seja, todas as UFs funcionarem em pools e só a escala do pool variar (testado no gate 1B; se ocorrer, a pergunta se reformula para o que determina o tamanho do pool).
Objection: a objeção mais forte é de medida. O `Código da Cozinha` tem granularidade variável (códigos EG, códigos CS com dezenas de nomes, "unidade gestora"). O grau registrado também trunca a cauda: nos projetos CDS com previsto ≥ 10, falta 0,45 das unidades previstas. As duas questões ficam para o relatório de dados (fase 4) e para a escolha do desfecho (fase 3). A segunda objeção é de independência: outro ano da mesma planilha compartilha organizações e superintendências com DATA1. O teste só vale com as previsões de cada UF e organização congeladas antes de abrir o dado novo, e com a dependência por organização tratada na fase 5.
Who cares: o trabalho acadêmico de quem conduz a pesquisa (IzaFerrari). A consequência é de conhecimento, com alcance de gestão: se a concentração vem do desenho administrativo do programa, a alavanca está na CONAB/MDS (regras das chamadas e das superintendências); se vem da escassez, está no recrutamento de mais organizações.
Non-goals: não estima efeito causal do regime sobre volume entregue, pessoas atendidas ou desempenho do programa; não fala de cozinhas físicas, só de unidades recebedoras registradas (códigos); não explica CDAF e CI (fora do recorte CDS); não confirma nem refuta nada com DATA1 (D-2); não define semanticamente os códigos CS/EG.

## Portfólio ativo

Linhagens adotadas da exploração (`pesquisa/exploracao/2026-10-21-explorer.md`), com o destino fixado na fase 3 (D-9):

1. **Regime de alocação por UF (pool denso × rede esparsa sobreposta)**, contra a escassez local. É a hipótese confirmatória **H1**. Era "pool × partição" na exploração e foi renomeada depois do gate 1B (D-7).
2. **Funil proposta → registro.** Não vira hipótese. Entra como checagem de H1 (K3: perda ≤ 0,3 por UF) e como descrição exploratória (H2, T7).
3. **Diluição × capacidade.** É a hipótese exploratória **H2**. Foi rebaixada na revisão do plano (D-9): a elasticidade grau–kg não discrimina os mecanismos, porque a proposta é montada para atender à demanda (MOC item 37) e o kg não é comparável entre produtos.

Rota, perecibilidade e complementaridade de cesta estão em `Deferred` no mapa (D-5). A diluição com uma medida de capacidade exógena também está lá (D-9).

## Compromissos congelados

### Hipóteses

- **H1** (confirmatória). Nas UFs elegíveis em que o regime de 2025 (DATA1) e a escassez do ano confirmatório (DATA2) preveem classes diferentes, o regime de DATA2 segue o de DATA1. Estimando **E1**; teste primário **T1**; sensibilidades T2 a T5. Regras, checagens e fronteira em `analysis-plan.md#h1`. Refutação: o regime de DATA2 segue a escassez em ≥ 75% das UFs discordantes.
- **H2** (exploratória). Elasticidade do grau em relação ao kg previsto, dentro da UF, em DATA1. Estimando **E2**; teste **T6**; especificação descritiva T7. Estado terminal previsto: `NOT_VERIFIED` (`analysis-plan.md#h2`).

### Estimandos

- **E1.** Na população de UFs elegíveis nos dois anos, sem as excluídas por K3, e restrita às UFs discordantes: a proporção cuja classe de regime em DATA2 coincide com a classe de DATA1, contra a proporção que coincide com a classe prevista pela razão unidades/organizações de DATA2 (limiar 1,725).
- **E2.** Em DATA1, nas organizações CDS com vínculo: a inclinação de log(grau registrado) em log(kg previsto) dentro da UF.

### Dados e população

- Descoberta: DATA1 (D-1), papel `discovery`, lido só das cópias com hash conferido.
- Confirmação: DATA2, a mesma planilha CONAB do PAA–Cozinhas de outro ano (2024 ou 2026), com o mesmo esquema. Não está identificado na data do congelamento (fase 4). Quando for, recebe hash e procedência **antes** de qualquer leitura do conteúdo, e a execução segue `analysis-plan.md#h1` sem mudanças.
- Recorte: projetos CDS. Ligação: `N° DO PROJETO` = `Num TPAF`. Vínculo: par distinto (CNPJ, `Código da Cozinha`). UF: a da organização.

### Saídas

- H1: `pesquisa/agregados/h1_<dado>.json`, gerado por `pesquisa/scripts/h1_confirmatorio.py`.
- H2: `pesquisa/agregados/h2_data1.json`, gerado por `pesquisa/scripts/h2_exploratorio.py`.

### Fronteira de interpretação

Os limites estão nos campos `May claim` / `May not claim` de cada hipótese em `analysis-plan.md`. Em resumo: nada causal; nada sobre a rota administrativa como mecanismo observado; nada sobre cozinhas físicas; nada confirmado com DATA1.
