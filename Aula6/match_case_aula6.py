##MATCH CASE

dia = int(input("Digite um número de 1 a 7: "))
match dia:
    case 1: 
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5:
        print("Quinta") 
    case 6:
        print("Sexta")
    case 7:
        print("Sábado") 
    case _:
        print("Dia inválido")
        

dia = int(input("Digite um número de 1 a 7: "))
if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda")
elif dia == 3:
    print("Terça")
elif dia == 4:
    print("Quarta")
elif dia == 5:
    print("Quinta")
elif dia == 6:
    print("Sexta")  
elif dia == 7:
    print("Sábado")
else:     
    print("Dia inválido")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operation = input("Digite a operação (+, -, *, /): ")

match operation:
    case "+":
        print(f"O resultado é: {num1 + num2}")
    case "-":
        print(f"O resultado é: {num1 - num2}")
    case "*":
        print(f"O resultado é: {num1 * num2}")
    case "/":
        if num2 != 0:
            print(f"O resultado é: {num1 / num2}")
        else:
            print("Erro: divisão por zero")
    case _:
        print("Operação inválida")
    
code = int(input("Digite um código de produto (10 a 14): "))

match code:
    case 10:
        print("Setor: Alimentos")
    case 11:
        print("Setor: Bebidas")
    case 12:
        print("Setor: Limpeza")
    case 13:
        print("Setor: Higiene")
    case 14:
        print("Setor: Hortifruti")
    case _:
        print("Código de produto inválido")


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

regiao = input("Digite a sigla da região (SP, RJ, MG ou OUTRAS_REGIÕES): ").upper()
match regiao:
    case "SP":
        valor_frete = 10.00
        prazo_dias = 2
    case "RJ":
        valor_frete = 15.00
        prazo_dias = 3
    case "MG":
        valor_frete = 18.00
        prazo_dias = 4
    case _:
        valor_frete = 50.00
        prazo_dias = 20
print(f"Valor do frete: R${valor_frete:.2f}")
print(f"Prazo de entrega: {prazo_dias} dias")