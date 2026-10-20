# 01 · Visão do produto

**ImobFlux** automatiza o caminho documental de um negócio imobiliário: do cadastro ao registro em cartório.

## Problema
Imobiliárias e corretores pequenos refazem à mão, a cada negócio, os mesmos passos: digitar dados de cliente e imóvel em um modelo de contrato, descobrir como pedir a guia de ITBI na prefeitura e explicar ao cliente o que fazer no cartório. Isso gera erros de digitação, contratos com dados divergentes da matrícula, retrabalho e clientes perdidos no processo.

## Solução
1. **Cadastro único** de clientes (pessoas) e imóveis; a IA lê fotos de RG, CNH, matrícula e IPTU e preenche os campos.
2. **Checagem de riscos antes do contrato** (IA): ônus na matrícula, débitos, divergências de nome e estado civil.
3. **Contratos automáticos**: locação e compra e venda, gerados a partir do cliente + imóvel já cadastrados (PDF e DOCX).
4. **Pedido de guia de ITBI** pré-preenchido (piloto: Valparaíso de Goiás), com acompanhamento do status.
5. **Roteiro até o registro**: passo a passo para o cliente, na ordem correta, com checklist de documentos.

## Público
- Cliente pagante: imobiliárias pequenas/médias e corretores autônomos no entorno do DF (piloto Valparaíso de Goiás).
- Usuário final do roteiro: comprador/vendedor/locatário (acessa por link, sem criar conta).

## Proposta de valor (uma frase)
"Do cadastro ao registro, sem retrabalho: contrato pronto, ITBI encaminhado e o cliente sabendo o próximo passo."

## Fora de escopo (MVP)
- Assinatura eletrônica própria (integrar depois, p.ex. ZapSign/Clicksign; no MVP o PDF é baixado).
- Pagamento de ITBI ou emolumentos dentro da plataforma.
- Protocolo eletrônico direto em cartório/prefeitura (sem API pública; o sistema só prepara e orienta).
- Gestão financeira de aluguéis (cobrança, repasse).
- Parecer jurídico: o sistema **não substitui advogado**; a IA aponta alertas, quem decide é o corretor/advogado.

## Métricas de sucesso do piloto
- Tempo para gerar um contrato completo: < 10 min (hoje: horas).
- Campos corrigidos manualmente após leitura por IA: < 15 %.
- Negócios com alerta de risco identificado antes da assinatura (medido, não prometido).
