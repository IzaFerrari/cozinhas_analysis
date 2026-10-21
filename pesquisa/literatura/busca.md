# Busca de literatura e de documentos — 2026-10-21

As consultas foram feitas em 2026-10-21, entre 19:40 e 20:00 UTC. Nenhuma ausência abaixo significa inexistência: significa "não encontrado nesta busca".

## Bases acadêmicas

| Id | Base | Consulta exata | Resultado |
|---|---|---|---|
| L1 | Scopus (scopus-research MCP, `advanced_search`, TITLE-ABS-KEY) | `"Programa de Aquisição de Alimentos" OR "Food Acquisition Program" OR "PAA" AND Brazil AND (procurement OR "family farming")` | 34 registros; 25 listados |
| L2 | Scopus (idem) | `"solidarity kitchen" OR "solidarity kitchens" OR "cozinha solidária" OR "cozinhas solidárias" OR "community kitchens" AND Brazil` | 5 registros |
| L3 | OpenAlex (lit-mcp B7; S2 falhou com HTTP 429, busca incompleta) | `"cozinhas solidárias" OR "cozinha solidária" OR "solidarity kitchens" AND Brasil` | 3 registros |
| L4 | OpenAlex + Semantic Scholar (lit-mcp B8) | `"Programa de Aquisição de Alimentos" AND ("doação simultânea" OR "unidades recebedoras" OR organizações)` | 30 únicos (OpenAlex 20 de 124; S2 14) |
| L5 | OpenAlex semântica (lit-mcp B9) | "How are supplier farmer organizations matched to recipient institutions in Brazil's Food Acquisition Program (PAA), and what explains how many recipient units each organization supplies?" | 25 |

Não consultados diretamente: SciELO, BDTD/teses, Google Acadêmico e relatórios IPEA fora do OpenAlex. A cobertura da literatura em português é parcial: o OpenAlex indexa parte da SciELO, não toda.

## Documentos normativos e institucionais (web)

| Id | Busca/fonte | Resultado |
|---|---|---|
| W1 | Busca web: planilha CONAB PAA–Cozinhas de projetos e unidades | Nenhuma planilha de outro ano encontrada; notícias regionais |
| W2 | Busca web: regras da proposta CDS para cozinhas | Manual de Operações da CONAB, Título 30 |
| W3 | Busca web: resoluções GGPAA sobre cozinhas | Resolução PAA/GG nº 7/2023; atas do GGPAA |
| W4 | Busca web: versões do Título 30 | Versão de 2026 (lida); versão anterior (Ato Dipai nº 05/2024; não verificamos se era a vigente em 2025) localizada, mas não obtida: o site antigo da CONAB tem certificado TLS inválido e devolveu HTML em vez de PDF; o Internet Archive respondeu 429 |
| W5 | Busca web ampla: planilhas de 2026 no gov.br/conab | Nenhuma planilha; notícias de 2026 (ver exposição abaixo) |

## Exposição registrada nesta busca

As buscas W1 e W5 trouxeram números de notícias sobre 2025 e 2026. Eles foram vistos antes de fixar o protocolo (D-9):
- PI, 2026: "21 Cozinhas Solidárias" e "12 organizações" selecionadas, o que dá uma razão de cerca de 1,75 unidades por organização; <!-- rm:ignore: número de notícia, registrado como exposição e não como resultado -->
- PR, 2025: "mais de 40 cozinhas solidárias" habilitadas; termos de pactuação para 22 e 4 cozinhas; <!-- rm:ignore: números de notícia, registrados como exposição -->
- RS: compra para 148 cozinhas solidárias (ano e modalidade não verificados). <!-- rm:ignore: número de notícia, registrado como exposição -->

Nenhum deles é o desfecho (forma do grafo organização–unidade). Os números de notícia não seguem as definições desta pesquisa: unidades com vínculo CDS e organizações com ao menos uma unidade.
