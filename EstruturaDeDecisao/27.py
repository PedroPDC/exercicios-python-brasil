# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
# receberá ainda um desconto de 10% sobre este total. 
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

kg_morangos = float(input("Por favor, insira a quantidade (em Kg) de morangos: "))
kg_macas = float(input("Por favor, insira a quantidade (em Kg) de maçãs: "))

if kg_morangos <= 5:
    preco_morango = 2.50
else:
    preco_morango = 2.20

if kg_macas <= 5:
    preco_maca = 1.80
else:
    preco_maca = 1.50

total_morango = kg_morangos * preco_morango
total_maca = kg_macas * preco_maca
total_compra = total_morango + total_maca

peso_total = kg_morangos + kg_macas
if peso_total > 8 or total_compra > 25:
    total_compra *= 0.90

print(f"\nValor a ser pago: R${total_compra}")


