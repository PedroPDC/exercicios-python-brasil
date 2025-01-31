# Faça um Programa que peça dois números e imprima o maior deles.

a = int(input("Por favor, insira o primeiro número: "))
b = int(input("Por favor, insira o segundo número: "))

if a > b:
    maior = a
    print(f"O maior número é: {maior}")
elif b > a:
    maior = b
    print(f"O maior número é: {maior}")
else:
    print(f"Os números são iguais")
