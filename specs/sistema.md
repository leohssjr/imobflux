# Spec do sistema ImobFlux (MVP)

Leia antes: `docs/01` a `docs/07`, `brand/BRAND.md`. Código em `app/`.

## Stack (padrão; pode trocar só com justificativa em `app/DECISIONS.md`)
- **Next.js 15 (App Router) + TypeScript + Tailwind CSS**, tokens de `brand/tokens.css`.
- **Prisma + SQLite** em dev (schema compatível com Postgres; `DATABASE_URL` configurável).
- **Auth**: e-mail + senha (Auth.js Credentials ou equivalente simples), multi-tenant por `Organization`.
- **IA**: SDK `@anthropic-ai/sdk`, visão para documentos; **modo mock** sem chave.
- **Documentos**: Handlebars → HTML → PDF (Playwright/Chromium) e DOCX (`docx`).
- **Validação**: zod. **Testes**: Vitest (unidade) + Playwright (um fluxo ponta a ponta).
- Idioma da UI: português do Brasil. Moeda BRL, datas dd/mm/aaaa.

## Modelo de dados (Prisma)
```
Organization(id, nome, cnpj?, plano, createdAt)
User(id, orgId, nome, email, senhaHash, papel[admin|corretor])
Person(id, orgId, nome, cpf, rg, rgOrgao, nascimento, nacionalidade, estadoCivil, regimeBens?, profissao, email, telefone, endereco(json), conjugeId?)
Property(id, orgId, tipo, enderecoCompleto(json), matricula, cartorio, inscricaoMunicipal, areaM2, valorVenal?, ownersJson, onusJson, observacoes)
Document(id, orgId, ownerType[person|property|deal], ownerId, tipo[rg|cnh|matricula|iptu|outro], storagePath, extractedJson, extractedAt, confirmedAt?, confirmedBy?)
Deal(id, orgId, tipo[locacao|compra_venda], formaPagamento[a_vista|financiado|parcelado]?, status, propertyId, partiesJson[{personId,papel}], valores(json), municipioId, createdBy, createdAt)
RiskAlert(id, dealId, tipo, gravidade[alta|media|baixa], mensagem, evidencia(json), reconhecidoPor?, reconhecidoEm?)
Contract(id, dealId, modeloVersao, dadosJson, pdfPath, docxPath, geradoEm)
ItbiRequest(id, dealId, municipioId, valorTransacao, baseCalculo, aliquota, estimativa, status[rascunho|solicitado|guia_online|via_fisica_retirada|paga], protocolo?, datas(json))
RoadmapStep(id, dealId, ordem, chave, titulo, descricao, status[pendente|feito], concluidoEm?)
AuditLog(id, orgId, userId, acao, entidade, entidadeId, em, detalhes(json))
```

## Telas e rotas
1. `/entrar`, `/registrar` — acesso e criação da organização.
2. `/` — painel: negócios por etapa, alertas pendentes, atalhos.
3. `/pessoas`, `/pessoas/novo`, `/pessoas/[id]` — cadastro com **upload de RG/CNH** e preenchimento por IA (tela de revisão com campo, valor lido e confiança; usuário confirma).
4. `/imoveis`, `/imoveis/novo`, `/imoveis/[id]` — idem com **matrícula e IPTU**.
5. `/negocios/novo` — assistente: tipo (locação/compra e venda) → forma de pagamento → imóvel → partes → valores.
6. `/negocios/[id]` — central do negócio com abas: **Resumo · Riscos · Contrato · ITBI · Roteiro · Histórico**.
   - Riscos: lista de alertas, botão "Conferir riscos" (IA), reconhecer alertas altos.
   - Contrato: pré-visualização, "Gerar PDF" e "Gerar DOCX" (bloqueado se faltar campo ou alerta alto sem reconhecimento).
   - ITBI (só compra e venda): dados pré-preenchidos, estimativa, PDF do pedido, status guiado (guia por e-mail → via física → paga).
   - Roteiro: etapas em ordem (escritura ou contrato bancário → ITBI → registro), checklist de documentos.
7. `/r/[token]` — **página pública do cliente** (sem login): roteiro do negócio, próximos passos e documentos necessários; somente leitura, token aleatório revogável.
8. `/configuracoes` — organização, usuários, municípios, marca (logo) nos PDFs.

## Requisitos funcionais (critérios de aceite)
- RF1 Cadastrar pessoa por foto de RG/CNH; valores lidos nunca são salvos sem confirmação.
- RF2 Cadastrar imóvel por foto de matrícula/IPTU; ônus e débitos extraídos viram dados estruturados.
- RF3 Conferir riscos gera `RiskAlert` para: ônus, débitos, divergência de nome, divergência de estado civil, campos ausentes.
- RF4 Contrato de locação e de compra e venda gerados em PDF e DOCX com dados de cliente + imóvel; falha com lista de campos faltantes.
- RF5 Valor por extenso correto (testes: 1, 100, 1.500, 250.000,50, 1.000.000).
- RF6 ITBI: lê parâmetros de `config/municipios/*.json`; estimativa = alíquota × base; aviso enquanto `verificado=false`.
- RF7 Roteiro respeita a ordem de `docs/02`; passo ITBI paga não pode ser marcado antes de escritura/financiamento.
- RF8 Página pública do cliente com token; revogar token em 1 clique.
- RF9 Multi-tenant: nenhuma consulta sem filtro por `orgId`; teste que prova isolamento.
- RF10 Audit log das ações de criar/confirmar/gerar/reconhecer.
- RF11 Exportar/excluir dados e documentos de uma pessoa (LGPD).

## Requisitos não funcionais
- Roda com `pnpm install && pnpm db:push && pnpm dev` **sem chaves** (IA em mock; PDF via Chromium local).
- Variáveis em `.env.example`: `DATABASE_URL`, `AUTH_SECRET`, `ANTHROPIC_API_KEY?`, `ANTHROPIC_MODEL?`, `STORAGE_DIR`, `LEGAL_REVIEWED=false`.
- Acessibilidade: contraste AA, foco visível, labels; responsivo (mobile primeiro para a página pública).
- Documentos pessoais em `STORAGE_DIR` privado, nunca em `public/`; servir por rota autenticada.
- Seed (`pnpm db:seed`): 1 organização, 1 usuário (`demo@imobflux.app` / `demo1234`, somente dev), 3 pessoas, 2 imóveis, 1 negócio de cada tipo, usando `fixtures/`.

## Identidade visual no produto
- Logo horizontal no topo da barra lateral; favicon e ícones de `brand/logo/web/` (copiar para `app/public/`).
- Botões primários teal (#0E7C7B), texto marinho, cantos 12 px, ícones de linha simples.
- PDFs: cabeçalho com logo da organização (ou ImobFlux), rodapé com aviso de revisão jurídica.

## Ordem de implementação sugerida
1. Scaffold, tokens, layout, auth, multi-tenant, seed.
2. Pessoas/imóveis (CRUD) + upload + IA mock → IA real.
3. Negócio + riscos.
4. Contratos (templates, extenso, PDF/DOCX).
5. ITBI + roteiro + página pública.
6. LGPD (exportar/excluir), audit, testes, README de `app/`.
7. Verificação final da checklist em `AGENTS.md`.
