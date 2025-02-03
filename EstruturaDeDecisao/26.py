# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# a) Álcool:
# b) até 20 litros, desconto de 3% por litro
# c) acima de 20 litros, desconto de 5% por litro
# d) Gasolina:
# e) até 20 litros, desconto de 4% por litro
# f) acima de 20 litros, desconto de 6% por litro 
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível 
# (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente 
# sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

litros_vendidos = float(input("Digite a quantidade de litros de combústivel: "))
tipo_combustivel = input("Qual o tipo de combustível? [A-álcool, G-gasolina]: ").upper()

if tipo_combustivel == "A":
    preco_total = litros_vendidos * 1.90
    if litros_vendidos <= 20:
        desconto = preco_total * 0.03
        preco_final = preco_total - desconto
        print(f"Você comprou {litros_vendidos} litros de Álcool, valor total: R${preco_final}")
    else:
        desconto = preco_total * 0.05
        preco_final = preco_total - desconto
        print(f"Você comprou {litros_vendidos} litros de Álcool, valor total: R${preco_final}")
elif tipo_combustivel == "G":
    preco_total = litros_vendidos * 2.50
    if litros_vendidos <= 20:
        desconto = preco_total * 0.04
        preco_final = preco_total - desconto
        print(f"Você comprou {litros_vendidos} litros de Gasolina, valor total: R${preco_final}")
    else:
        desconto = preco_total * 0.06
        preco_final = preco_total - desconto
        print(f"Você comprou {litros_vendidos} litros de Gasolina, valor total: R${preco_final}")
else:
    print("Insira um tipo de combústivel válido!")