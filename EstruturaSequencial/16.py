# Faça um programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e 
# que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

tamanho = float(input("Por favor, informe o tamanho em METROS QUADRADOS da área a ser pintada: "))
cobertura = tamanho / 3
latas = int(cobertura / 18)
total = latas * 80

print(f"Você deverá comprar {latas} lata(s) de tinta, preço total R${total}")