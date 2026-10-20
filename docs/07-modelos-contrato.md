# 07 · Modelos de contrato (esqueletos)

> **Aviso**: texto-base para o sistema funcionar. Deve ser **revisado por advogado** antes de uso real. O sistema exibe esse aviso no rodapé do PDF enquanto `LEGAL_REVIEWED=false`.

Variáveis entre `{{ }}` (Handlebars). Cláusulas condicionais com `{{#if}}`. Os modelos finais vivem em `app/templates/` (`locacao.hbs`, `compra-venda.hbs`).

## Locação residencial (Lei 8.245/91)
Cabeçalho: CONTRATO DE LOCAÇÃO RESIDENCIAL.
Partes: LOCADOR `{{locador.nome}}`, `{{locador.nacionalidade}}`, `{{locador.estado_civil}}`, CPF `{{locador.cpf}}`, RG `{{locador.rg}}`, residente em `{{locador.endereco}}`; LOCATÁRIO (idem). Se casado(a): incluir cônjuge `{{#if conjuge}}`. FIADOR (se garantia = fiador).
Cláusulas:
1. **Objeto**: imóvel `{{imovel.endereco_completo}}`, matrícula nº `{{imovel.matricula}}` do `{{imovel.cartorio}}`, inscrição municipal `{{imovel.inscricao_municipal}}`.
2. **Finalidade**: residencial.
3. **Prazo**: `{{prazo_meses}}` meses, de `{{inicio}}` a `{{fim}}`.
4. **Aluguel**: R$ `{{valor_aluguel}}` (`{{valor_extenso}}`), vencimento dia `{{dia_vencimento}}`, reajuste anual por `{{indice_reajuste}}`.
5. **Encargos**: IPTU, condomínio, água, luz por conta do `{{responsavel_encargos}}`.
6. **Garantia**: `{{garantia.tipo}}` (caução até 3 meses / fiador / seguro-fiança / título de capitalização), detalhes `{{garantia.detalhes}}`.
7. **Conservação e vistoria**: laudo de vistoria anexo.
8. **Multa por rescisão antecipada**: proporcional ao prazo restante, equivalente a `{{multa_meses}}` aluguéis (art. 4º).
9. **Venda do imóvel** e cláusula de vigência: `{{#if clausula_vigencia}}…{{/if}}` (art. 8º).
10. **Foro**: comarca de `{{foro}}`.
Assinaturas: partes e 2 testemunhas.

## Compra e venda de imóvel
Cabeçalho: INSTRUMENTO PARTICULAR DE PROMESSA/COMPRA E VENDA (escolher `{{tipo_instrumento}}`).
Partes: VENDEDOR(ES) e COMPRADOR(ES) (qualificação completa + cônjuges).
Cláusulas:
1. **Objeto**: imóvel e matrícula (como acima), área `{{imovel.area}}` m².
2. **Preço e pagamento**: R$ `{{preco}}`; forma `{{forma_pagamento}}` (à vista / financiado `{{banco}}` / parcelado); sinal e datas.
3. **Declarações do vendedor**: imóvel livre de ônus, exceto `{{onus_declarados}}`; débitos até a data da posse por conta do vendedor.
4. **Escritura/Financiamento**: prazo para escritura `{{prazo_escritura}}` dias (à vista) ou contrato bancário (financiado).
5. **ITBI e registro**: ITBI e emolumentos por conta do `{{responsavel_itbi}}` (padrão: comprador), valor estimado R$ `{{itbi_estimado}}`.
6. **Posse**: entrega em `{{data_posse}}`.
7. **Multa e rescisão**: `{{multa_percentual}}`%.
8. **Foro**: `{{foro}}`.
Assinaturas: partes, cônjuges, 2 testemunhas.

## Regras de geração
- Falha se faltar campo obrigatório; listar os faltantes.
- Valor por extenso gerado em código (pt-BR), não pela IA.
- Datas no formato "19 de outubro de 2026".
- Guardar o JSON de dados usado + versão do modelo para reprodutibilidade.
