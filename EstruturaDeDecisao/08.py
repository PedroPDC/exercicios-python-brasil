# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato

a = float(input("Digite o preço do primeiro produto: "))
b = float(input("Digite o preço do segundo produto: "))
c = float(input("Digite o preço do terceiro produto: "))

menor = a

if b < menor:
    menor = b
    print(f"\nVocê deverá comprar o segundo produto, pois ele custa: R${menor}")
if c < menor:
    menor = c
    print(f"\nVocê deverá comprar o terceiro produto, pois ele custa: R${menor}")
if a == menor:
    print(f"\nVocê deverá comprar o primeiro produto, pois ele custa: R${menor}")

