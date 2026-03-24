# -*- coding: utf-8 -*-
## DESAFIO E-COMMERCE
## UMA PLATAFORMA DE E-COMMERCE PRECISA CALCULAR O VALOR DO FRETE E O PRAZO DE ENTREGA COM BASE NA REGIÃO DO BRASIL
## (SIGLA COM 2 LETRAS). CRIE UM PROGRAMA QUE RECEBA A REGIÃO E DEFINA AS VARIÁVEIS VALOR_FRETE(FLOAT) E PRAZO_DIAS(INT)

SP_FRETE = 10.00
SP_PRAZO = 2
RJ_FRETE = 15.00
RJ_PRAZO = 3
MG_FRETE = 18.00
MG_PRAZO = 4
OUTRAS_FRETE = 50.00
OUTRAS_PRAZO = 20

regiao = input("Digite a sigla da regiao (SP, RJ, MG ou OUTRAS_REGIOES): ").upper()
match regiao:
    case "SP":
        valor_frete = SP_FRETE
        prazo_dias = SP_PRAZO
    case "RJ":
        valor_frete = RJ_FRETE
        prazo_dias = RJ_PRAZO
    case "MG":
        valor_frete = MG_FRETE
        prazo_dias = MG_PRAZO
    case _:
        valor_frete = OUTRAS_FRETE
        prazo_dias = OUTRAS_PRAZO
print(f"Valor do frete: R${valor_frete:.2f}")
print(f"Prazo de entrega: {prazo_dias} dias")