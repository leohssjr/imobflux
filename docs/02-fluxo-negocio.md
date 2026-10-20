# 02 · Fluxo de negócio (validado com corretor/cartório)

> Fonte: orientação de um profissional do setor (Pietro) e conversas do projeto. Itens marcados ⚠️ precisam de confirmação oficial.

## Compra e venda à vista
1. **Escritura no cartório de notas** (a escritura é paga antes de recolher a guia).
2. **Guia de ITBI**: sai online por e-mail da prefeitura; depois é preciso **retirar a via física** na prefeitura; pagar.
3. **Registro no cartório de registro de imóveis** (com escritura + guia de ITBI paga).

## Compra e venda financiada
Mesma ordem: 1) **contrato assinado no banco** (contrato de financiamento tem força de escritura); 2) retirar e pagar a guia de ITBI; 3) registrar no cartório de registro de imóveis.

## Locação
Contrato de locação (Lei 8.245/91) com garantia (caução, fiador, seguro-fiança ou título de capitalização). Não há ITBI. Registro do contrato na matrícula é opcional (necessário para exigir vigência em caso de venda do imóvel, com cláusula de vigência).

## O que o ImobFlux faz em cada etapa
| Etapa | Ação do sistema |
|---|---|
| Antes de tudo | Cadastro por foto de documentos + checagem de riscos (IA) |
| Contrato | Gera PDF/DOCX a partir do modelo; vincula partes e imóvel |
| Escritura (à vista) | Gera ficha/checklist para o cartório de notas |
| ITBI | Gera o pedido pré-preenchido; registra e-mail recebido; lembra retirada da via física e pagamento |
| Registro | Checklist de documentos e roteiro passo a passo |

## Máquina de estados do negócio (`Deal.status`)
`rascunho → analise_riscos → contrato_gerado → assinado → escritura_ou_financiamento → itbi_solicitado → itbi_guia_online → itbi_via_fisica_retirada → itbi_paga → registro_protocolado → concluido` (a qualquer momento: `cancelado`).
- Locação usa apenas: `rascunho → analise_riscos → contrato_gerado → assinado → concluido`.
- Compra e venda à vista e financiada usam o mesmo caminho; o passo `escritura_ou_financiamento` muda o texto do roteiro.

## Ordem dos passos no roteiro do cliente (compra e venda)
Sempre na ordem: (1) escritura ou contrato bancário, (2) guia de ITBI (online → retirar física → pagar), (3) registro. O sistema **não deve** permitir marcar ITBI paga antes de "escritura/financiamento" concluído.
