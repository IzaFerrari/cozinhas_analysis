# Protocolo — Por que algumas organizações fornecedoras do PAA–Cozinhas atendem muito mais unidades

Estado: rascunho (fase 1). Nada está congelado. O congelamento é da fase 3.

## Question

Por que algumas organizações fornecedoras de projetos CDS do PAA–Cozinhas da CONAB atendem muito mais unidades recebedoras do que outras? Em particular, o grau alto em AL, PB e RN vem de uma regra de montagem das propostas própria da UF (pool de unidades compartilhado) ou da escassez local de organizações em relação às unidades?

Claim: associational
Unit of analysis: a organização fornecedora (CNPJ) com projeto CDS–Cozinhas na planilha da CONAB, para o grau; e a UF, para o regime de alocação.
Estimand: em dado independente de DATA1 (D-2), há dois contrastes. (i) Entre UFs: a associação entre a forma do grafo organização–unidade (índice de compartilhamento ajustado por tamanho, a fixar na fase 3) e a razão unidades/organizações, comparada com a persistência do regime de cada UF previsto a partir de DATA1 e congelado antes de abrir o dado novo. (ii) Entre organizações, dentro do regime: a elasticidade do grau em relação à quantidade prevista (kg). O desfecho é o grau previsto ou o registrado; a escolha é fixada na fase 3 (linhagem 2 da exploração).
Refutation: a pergunta fica errada ou bem mais estreita se (a) não houver dado independente adequado, isto é, outro ano da mesma planilha ou projetos novos (as hipóteses terminam em `BLOCKED` e o que vier de DATA1 é só exploratório, D-3); (b) documentos das chamadas mostrarem uma regra nacional única em que a organização escolhe livremente as unidades (aí "regra da UF" deixa de ser candidata e a pergunta passa a ser por que as organizações escolhem assim); (c) a diferença entre UFs sumir quando o grafo é dividido em componentes conexos, ou seja, todas as UFs funcionarem em pools e só a escala do pool variar (testado no gate 1B; se ocorrer, a pergunta se reformula para o que determina o tamanho do pool).
Objection: a objeção mais forte é de medida. O `Código da Cozinha` tem granularidade variável (códigos EG, códigos CS com dezenas de nomes, "unidade gestora"). O grau registrado também trunca a cauda: nos projetos CDS com previsto ≥ 10, falta 0,45 das unidades previstas. As duas questões ficam para o relatório de dados (fase 4) e para a escolha do desfecho (fase 3). A segunda objeção é de independência: outro ano da mesma planilha compartilha organizações e superintendências com DATA1. O teste só vale com as previsões de cada UF e organização congeladas antes de abrir o dado novo, e com a dependência por organização tratada na fase 5.
Who cares: o trabalho acadêmico de quem conduz a pesquisa (IzaFerrari). A consequência é de conhecimento, com alcance de gestão: se a concentração vem do desenho administrativo do programa, a alavanca está na CONAB/MDS (regras das chamadas e das superintendências); se vem da escassez, está no recrutamento de mais organizações.
Non-goals: não estima efeito causal do regime sobre volume entregue, pessoas atendidas ou desempenho do programa; não fala de cozinhas físicas, só de unidades recebedoras registradas (códigos); não explica CDAF e CI (fora do recorte CDS); não confirma nem refuta nada com DATA1 (D-2); não define semanticamente os códigos CS/EG.

## Portfólio ativo

Linhagens adotadas da exploração (`pesquisa/exploracao/2026-10-21-explorer.md`); as hipóteses só se fixam na fase 3:

1. **Regime de alocação por UF (pool denso × rede esparsa sobreposta).** É a hipótese explicativa central, contra a escassez local. Era "pool × partição" na exploração; foi renomeada depois do gate 1B (D-7), que achou territórios exclusivos raros.
2. **Funil proposta → registro.** Condição de medida: define se o desfecho é o grau previsto ou o registrado, e como tratar a perda que cresce com o tamanho do projeto.
3. **Diluição × capacidade.** Assinatura quantitativa: a elasticidade do grau em relação à oferta separa atribuição de oferta empurrada.

Rota, perecibilidade e complementaridade de cesta estão em `Deferred` no mapa (D-5).
