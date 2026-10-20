# 03 · ITBI — piloto Valparaíso de Goiás

Parâmetros do piloto (configuráveis em `config/municipios/valparaiso-de-goias.json`; ver `specs/sistema.md`).

| Parâmetro | Valor | Status |
|---|---|---|
| Alíquota | 2 % | ⚠️ obtida de calculadora não oficial; confirmar com a Secretaria de Finanças |
| Base de cálculo | maior valor entre valor venal e valor da transação | ⚠️ confirmar (regra comum, varia por município) |
| Entrega da guia | Online por e-mail; retirada da via física na prefeitura | ✅ informado por profissional do setor |
| Quem paga | Comprador (costume; negociável por contrato) | ✅ costume |
| Documentos usuais | Escritura/contrato, matrícula atualizada, IPTU, documentos das partes | ⚠️ confirmar lista oficial |

## Regras de implementação
- Nunca cravar alíquota ou prazos no código; ler do JSON do município e exibir aviso "valores estimados — confirme com a prefeitura" enquanto `verificado: false`.
- O "pedido de ITBI" é um **documento/resumo pré-preenchido** (transmitente, adquirente, imóvel, valor, inscrição municipal) que o corretor usa no atendimento ou envia por e-mail. Não há integração com sistema da prefeitura no MVP.
- Estimativa de imposto = alíquota × base. Mostrar como estimativa.
- Para adicionar novo município: copiar o JSON, preencher e marcar `verificado` somente após confirmação por escrito.
