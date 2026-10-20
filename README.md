<p align="center"><img src="brand/logo/svg/imobflux-horizontal.svg" alt="ImobFlux" height="64"></p>

# ImobFlux

**Do cadastro ao registro, sem retrabalho.** Sistema que gera contratos de locação e de compra e venda a partir de clientes e imóveis já cadastrados, prepara o pedido da guia de ITBI (piloto: Valparaíso de Goiás) e guia o cliente até o cartório. IA restrita a duas funções: ler RG, CNH, matrícula e IPTU, e conferir riscos antes do contrato.

Projeto para o **SEBRAE Supernova**.

## Como usar este repositório com uma IA
Abra o repositório em uma ferramenta de IA com acesso a arquivos e terminal (Claude Code, Codex, Cursor…) e peça:

> Implemente o projeto.

A IA vai ler `AGENTS.md` e construir:
- o **sistema** em `app/` (spec: `specs/sistema.md`);
- o **slide de pitch** em `pitch/` (spec: `specs/pitch.md`), já com a logo e a identidade visual.

Prompts prontos (só sistema, só pitch, revisão) estão em `prompts/`.

## Mapa do repositório
| Pasta | Conteúdo |
|---|---|
| `AGENTS.md` / `CLAUDE.md` | Instruções mestras para a IA e checklist de pronto |
| `docs/` | Visão, fluxo de negócio, ITBI, IA, mercado, BMC, modelos de contrato |
| `specs/` | Especificação do sistema, do pitch e prompts de IA |
| `brand/` | Logo (kit completo), cores, fontes, regras de uso |
| `config/` | Parâmetros por município (ITBI) |
| `fixtures/` | Orientações de dados fictícios para seed e testes |
| `app/` | Destino do sistema (a IA cria aqui) |
| `pitch/` | Destino da apresentação (a IA cria aqui) |

## Pontos a confirmar antes de uso real
- Alíquota e regras de ITBI de Valparaíso de Goiás (hoje 2 %, fonte não oficial).
- Revisão dos modelos de contrato por advogado.
- Busca de anterioridade da marca no INPI.
- Preços do mercado e hipóteses de preço do ImobFlux (`docs/05-mercado.md`).
