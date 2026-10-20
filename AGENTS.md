# AGENTS.md — instruções para IA (Claude, Codex, Cursor etc.)

Você está no repositório do **ImobFlux**. Se o usuário pedir "implemente o projeto" (ou algo equivalente), entregue **duas coisas**:

1. **O sistema** em `app/` seguindo `specs/sistema.md`.
2. **O pitch** em `pitch/` seguindo `specs/pitch.md`, com a logo e a identidade de `brand/`.

## Ordem de leitura obrigatória
1. `README.md` → visão geral.
2. `docs/01-visao.md`, `docs/02-fluxo-negocio.md`, `docs/03-itbi-valparaiso.md`, `docs/04-ia.md`.
3. `docs/05-mercado.md`, `docs/06-bmc.md`, `docs/07-modelos-contrato.md`.
4. `brand/BRAND.md`, `brand/tokens.css`, `brand/logo/GUIA-DE-USO.md`.
5. `specs/sistema.md`, `specs/ai-prompts.md`, `specs/pitch.md`.

## Como trabalhar
- Faça um plano curto, depois implemente em passos verificáveis (ordem em `specs/sistema.md`). Rode o que construir: instalar, `db:push`, seed, testes, `build`.
- Se a ferramenta permitir subagentes, o sistema e o pitch podem ser feitos em paralelo (pastas independentes). O pitch lê só `docs/05`, `docs/02`, `docs/04` e `brand/`.
- Decisões que fujam do spec: registre em `app/DECISIONS.md` (1 linha cada, com motivo).
- Dúvida sem resposta nos docs: escolha o padrão mais simples, marque `TODO(confirmar)` e liste no relatório final. **Não pergunte** a menos que algo seja irreversível.
- Commits pequenos e em português ("feat: cadastro de pessoas com leitura de RG"). Não commitar `.env`, bancos, documentos reais.

## Regras que não podem ser quebradas
- IA **apenas** nas duas funções de `docs/04-ia.md`. Sem chat livre, sem redação de cláusulas por IA.
- Nunca cravar alíquota de ITBI, prazos ou regras municipais no código: ler de `config/municipios/*.json`; manter aviso enquanto `verificado=false`.
- Ordem do fluxo: escritura/contrato bancário → ITBI (guia online → via física → paga) → registro.
- Nunca inventar dados de mercado, depoimentos ou métricas no pitch.
- O sistema não dá parecer jurídico; modelos exigem revisão de advogado (`LEGAL_REVIEWED`).
- Dados pessoais: sem logar conteúdo de documentos; storage privado; filtro por `orgId` em toda consulta.
- Logo e cores só dos arquivos de `brand/`; nunca redesenhar nem redigitar o nome.
- Tudo roda sem chaves (IA em mock) e sem serviços externos.
- Documentos e UI em português do Brasil.

## Definição de pronto (checklist final)
- [ ] `cd app && pnpm install && pnpm db:push && pnpm db:seed && pnpm dev` funciona do zero; `pnpm test` e `pnpm build` passam.
- [ ] Fluxo ponta a ponta no navegador: cadastrar pessoa por foto (mock) → imóvel → negócio → riscos → contrato PDF/DOCX → ITBI → roteiro → página pública `/r/[token]`.
- [ ] Teste de isolamento entre organizações passa; teste do valor por extenso passa.
- [ ] `app/README.md` com como rodar, variáveis, arquitetura em 10 linhas.
- [ ] `pitch/index.html` com 12 slides e `pitch/imobflux-pitch.pdf` de 12 páginas, revisados por screenshot.
- [ ] Relatório final (≤ 15 linhas): o que foi feito, o que ficou como `TODO(confirmar)`, como rodar e apresentar.
