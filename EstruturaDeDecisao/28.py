# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
# porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o 
# cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e 
# a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: 
# tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

print("Tipos de carne disponíveis:")
print("1 - Filé Duplo")
print("2 - Alcatra")
print("3 - Picanha")

opcao = int(input("Escolha o tipo de carne (1, 2, 3): "))
quant = float(input("Digite a quantidade (em Kg): "))

if opcao == 1:
    tipo_carne = "Filé Duplo"
    preco_kg = 4.90 if quant <= 5 else 5.80
elif opcao == 2:
    tipo_carne = "Alcatra"
    preco_kg = 5.90 if quant <= 5 else 6.80
elif opcao == 3:
    tipo_carne = "Picanha"
    preco_kg = 6.90 if quant <= 5 else 7.80
else:
    print("opção inválida!")
    exit()

valor_total = quant * preco_kg

pagamento = input("Pagamento com o cartão Tabajara? (sim/não): ").strip().lower()
if pagamento == "sim" or pagamento == "s":
    desconto = valor_total * 0.05
    tipo_pagamento = "Cartão Tabajara"
else:
    desconto = 0
    tipo_pagamento = "Outro"

valor_final = valor_total - desconto

print("\n--- CUPOM FISCAL ---")
print(f"Tipo de Carne: {tipo_carne}")
print(f"Quantidade: {quant} Kg")
print(f"Preço por Kg: R${round(preco_kg, 2)}")
print(f"Preço total: R${round(valor_total, 2)}")
print(f"Tipo de pagamento: {tipo_pagamento}")
print(f"Desconto: R${round(desconto, 2)}")
print(f"Valor a pagar: R${round(valor_final, 2)}")