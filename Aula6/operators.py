# você tem uma lista de ferramentes e precisa criar uma nova lista apenas
# com as vendas de maior valor (acima de 500)

vendas = [120, 800, 450, 1200, 30, 600]
vendas_grandes = []

for valor in vendas:
    if valor > 500:
        vendas_grandes.append(valor)

print(f'Vendas: {vendas_grandes}')