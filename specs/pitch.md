# Spec do pitch ImobFlux (slides)

**Entregável**: `pitch/index.html` — apresentação 16:9 em **um único arquivo HTML autocontido** (CSS/JS inline, logo em SVG inline, fontes Poppins/Inter via Google Fonts com fallback de sistema), mais `pitch/imobflux-pitch.pdf` exportado via Chromium (1920×1080, 1 slide por página) e `pitch/README.md` (como abrir, apresentar e exportar).
Público: avaliadores do **SEBRAE Supernova** (negócios, não técnicos). Duração: 5 minutos, 12 slides.

## Regras de design (bem estilizado)
- Use `brand/tokens.css` (copiar para dentro do HTML) e a logo de `brand/logo/svg` (inline). Leia `brand/BRAND.md`.
- Slides alternam fundo **branco/#F6F8F8** e **marinho #0F1B2D**; nos escuros use a logo reversed e menta #7FD6D3 como destaque. Capa e fechamento em marinho com símbolo grande recortado/ampliado como elemento gráfico (opacidade baixa).
- Tipografia: títulos Poppins 700 (48–72 px em 1920 px), corpo Inter 400/500 (24–30 px). No máximo 1 ideia por slide, no máximo ~25 palavras de corpo.
- Linguagem visual: ângulos retos e 45° (eco da Casa F), cantos de 12 px, cartões com borda `--if-line`, ícones de linha geométricos em SVG próprio, **sem clipart e sem imagens de banco**.
- Visualizações feitas em SVG/HTML: linha do tempo do fluxo (cadastro → riscos → contrato → ITBI → registro), mockup do produto desenhado em HTML (não captura de tela falsa), comparação de concorrentes em tabela.
- Animações sutis (entrada com fade/translate 300 ms, `prefers-reduced-motion` respeitado). Sem bibliotecas pesadas.
- Navegação: setas, espaço, toque/swipe, `F` tela cheia, `?print` para modo impressão; indicador de progresso fino em teal; contador "n/12".
- Escala: palco fixo 1920×1080 escalado por `transform: scale()` para caber em qualquer tela, centralizado.
- Acessibilidade: contraste AA, `lang="pt-BR"`, ordem de leitura lógica, `alt`/`aria-label` na logo.
- Número de slide e logo pequena discretos no rodapé (exceto capa/fechamento).

## Roteiro dos 12 slides (texto base em pt-BR; pode lapidar, não inventar números)
1. **Capa** — logo grande · "Do cadastro ao registro, sem retrabalho." · "SEBRAE Supernova · [nome da equipe]".
2. **O problema** — "Cada negócio imobiliário recomeça do zero." Três dores: dados digitados várias vezes; contrato com erro; cliente perdido entre prefeitura e cartório.
3. **Quem sente** — corretores e imobiliárias pequenas; frase de dor (usar só se houver depoimento real de entrevista; senão, descrever o perfil).
4. **A solução** — ImobFlux em uma frase + linha do tempo de 5 etapas: Cadastro · Riscos · Contrato · ITBI · Registro.
5. **Como funciona** — mockup HTML do produto: foto do documento → campos preenchidos com confiança → botão "Gerar contrato".
6. **IA com propósito** — só duas funções: (1) ler RG, CNH, matrícula e IPTU; (2) conferir riscos: ônus, débitos, divergência de nome e estado civil. "A IA alerta, o profissional decide."
7. **Do contrato ao cartório** — fluxo correto: à vista (escritura → ITBI → registro) e financiado (contrato no banco → ITBI → registro); ITBI: guia por e-mail, retirada da via física, pagamento. Piloto: Valparaíso de Goiás.
8. **Mercado e lacuna** — tabela de concorrentes de `docs/05-mercado.md` (Jetimob, Superlógica, ZapSign, advogado, Conecta) e a lacuna: ninguém cobre ITBI + registro para o corretor pequeno. Só preços com fonte; rotular "preços de referência".
9. **Modelo de negócio** — planos (Starter/Pro/por contrato) marcados como **hipótese de preço**, comissão de parceiros.
10. **Validação e próximos passos** — o que já foi validado (fluxo com profissional do setor) e o que falta (confirmar alíquota/documentos com a prefeitura, 10 entrevistas, protótipo com 1 imobiliária). Marco de 90 dias.
11. **Riscos e cuidados** — LGPD, revisão por advogado, não substitui parecer jurídico; como mitigamos.
12. **Fechamento** — logo grande, "ImobFlux · Contratos, ITBI e registro sem retrabalho", contatos `[preencher]`.

## Regras de conteúdo
- Nunca inventar dados de mercado, depoimentos, clientes ou métricas. Se faltar, escrever "a validar" de forma elegante (selo "hipótese") ou omitir.
- Usar apenas números de `docs/05-mercado.md` e citar a fonte em rodapé pequeno no slide.
- Português do Brasil, tom claro e confiante, sem jargão jurídico.

## Critérios de aceite
- Abre offline (exceto fontes, com fallback) e funciona em 1920×1080 e 1366×768 e no celular em modo paisagem.
- PDF exportado com 12 páginas, sem cortes, logo nítida.
- Capturar screenshots de cada slide e revisar visualmente (sem sobreposição, sem texto cortado, contraste OK) antes de entregar.
- Peso < 1 MB (sem imagens raster).
