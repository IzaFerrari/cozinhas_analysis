# Protocolo — Como as organizações fornecedoras do PAA–Cozinhas se ligam às unidades recebedoras (2025)

Estado: congelado (fase 3, D-10; reaberto e recongelado na D-12, na D-16 e na D-17; escopo descritivo na D-22; H3 descritiva e limitação de H1 na D-23). Mudança material só por bloco novo em `decisoes.md` (CHANGE_PLAN). O congelamento é o commit que traz este estado junto com `analysis-plan.md` em `Freeze: frozen`. Registro: interno, `pesquisa/registro.md` (D-10).

## Question

Como as organizações fornecedoras de projetos CDS do PAA–Cozinhas da CONAB se ligam às unidades recebedoras em 2025: quantas unidades cada organização atende, como os vínculos se organizam em cada UF e quanto do previsto nas propostas aparece registrado? A pergunta explicativa original (regra da UF × escassez local) segue registrada como H1, bloqueada (D-22).

Claim: descriptive
Unit of analysis: a organização fornecedora (CNPJ) com projeto CDS–Cozinhas no snapshot DATA1, para o grau; a UF da organização, para a estrutura dos vínculos; o projeto, para a perda previsto→registrado.
Estimand: censo do snapshot DATA1 (D-1), sem inferência amostral. E3: distribuição do grau (mediana, média, decis, máximo, proporção com grau 1). E4: por UF elegível (≥ 10 unidades e ≥ 3 organizações), participação de pool, razão unidades/organizações e concordância entre as duas. E5: perda previsto→registrado, no total, por faixa de tamanho do projeto e por UF.
Refutation: a descrição fica errada ou bem mais estreita se o `Código da Cozinha` não identificar unidades de modo consistente (granularidade), ou se o snapshot não representar o programa de 2025 porque o registro ainda está incompleto (planilha viva, D-21).
Objection: a objeção mais forte é de medida. Os códigos EG reúnem cozinhas, e o registro é incompleto nos projetos grandes. Ambas são tratadas no relatório de dados e nas limitações. A segunda objeção: as escolhas de medida foram feitas depois de ver os dados (D-2), o que está declarado.
Who cares: o trabalho acadêmico de quem conduz a pesquisa (IzaFerrari), e a gestão do PAA–Cozinhas (CONAB/MDS), que ganha um retrato de como os fornecedores se distribuem entre as cozinhas.
Non-goals: não explica por que os padrões existem (H1, bloqueada); não faz inferência causal; não avalia volume, valor ou pessoas atendidas; não fala de cozinhas físicas; não cobre CDAF e CI na estrutura dos vínculos.

## Portfólio ativo

Linhagens adotadas da exploração (`pesquisa/exploracao/2026-10-21-explorer.md`), com o destino fixado na fase 3 (D-9):

1. **Regime de alocação por UF (pool denso × rede esparsa sobreposta)**, contra a escassez local. É a hipótese confirmatória **H1**. Era "pool × partição" na exploração e foi renomeada depois do gate 1B (D-7).
2. **Funil proposta → registro.** Não vira hipótese. Entra como checagem de H1 (K3: perda ≤ 0,3 por UF) e como descrição exploratória (H2, T7).
3. **Diluição × capacidade.** É a hipótese exploratória **H2**. Foi rebaixada na revisão do plano (D-9): a elasticidade grau–kg não discrimina os mecanismos, porque a proposta é montada para atender à demanda (MOC item 37) e o kg não é comparável entre produtos.

Rota, perecibilidade e complementaridade de cesta estão em `Deferred` no mapa (D-5). A diluição com uma medida de capacidade exógena também está lá (D-9).

## Compromissos congelados

### Hipóteses

- **H1** (confirmatória). Nas UFs utilizáveis que em 2025 (DATA1) estavam do lado da faixa de escassez correspondente à sua classe e cuja razão unidades/organizações, no ano confirmatório, sai da faixa (1,45; 2,00) para o lado oposto, o regime do ano confirmatório segue o de 2025 (D-17). Estimando **E1**; teste primário **T1**; sensibilidades T2 a T5. Regras, checagens e fronteira em `analysis-plan.md#h1`. Refutação: o regime de DATA2 segue a escassez em ≥ 75% das UFs discordantes.
- **H2** (exploratória). Elasticidade do grau em relação ao kg previsto, dentro da UF, em DATA1. Estimando **E2**; teste **T6**; especificação descritiva T7. Estado terminal previsto: `NOT_VERIFIED` (`analysis-plan.md#h2`).

### Estimandos

- **E1.** Na população de UFs utilizáveis (elegíveis nos dois anos, sem as excluídas por K7, K3 e exposição, e sem as herdadas; D-12, D-16, D-18), e restrita às UFs discordantes, isto é, as que saem da faixa de escassez (1,45; 2,00) para o lado oposto ao da sua classe (D-17): a proporção cuja classe de regime em DATA2 coincide com a classe de DATA1, contra a proporção que coincide com a classe prevista pela razão unidades/organizações de DATA2 (faixa de 1,45 a 2,00; D-17).
- **E2.** Em DATA1, nas organizações CDS com vínculo: a inclinação de log(grau registrado) em log(kg previsto) dentro da UF. Desde a D-23 é tratada como descrição; o IC agrupado é uma aproximação descritiva da variação entre UFs, não inferência para uma população.
- **E3** (descritivo, D-22). Distribuição do grau por organização CDS em DATA1 (R3).
- **E4** (descritivo, D-22, D-23). Estrutura dos vínculos por UF elegível: vínculos por organização, organizações por unidade, cobertura, componentes, participação de pool e a sua associação com o nº de organizações e a razão (H3, T8).
- **E5** (descritivo, D-22). Perda previsto→registrado no total, por faixa de tamanho e por UF (R3, R6).

### Dados e população

- Descoberta: DATA1 (D-1), papel `discovery`, lido só das cópias com hash conferido.
- Confirmação: DATA2, a mesma planilha CONAB do PAA–Cozinhas de outro ano (2024 ou 2026), com o mesmo esquema. Não está identificado na data do congelamento (fase 4). Quando for, recebe hash e procedência **antes** de qualquer leitura do conteúdo, e a execução segue `analysis-plan.md#h1` sem mudanças.
- Recorte: projetos CDS. Ligação: `N° DO PROJETO` = `Num TPAF`. Vínculo: par distinto (CNPJ, `Código da Cozinha`). UF: a da organização.

### Saídas

- H1: `pesquisa/agregados/h1_<dado>.json`, gerado por `pesquisa/scripts/h1_confirmatorio.py`.
- H2: `pesquisa/agregados/h2_data1.json`, gerado por `pesquisa/scripts/h2_exploratorio.py`.

### Fronteira de interpretação

Os limites estão nos campos `May claim` / `May not claim` de cada hipótese em `analysis-plan.md`. Em resumo: nada causal; nada sobre a rota administrativa como mecanismo observado; nada sobre cozinhas físicas; nada confirmado com DATA1.
