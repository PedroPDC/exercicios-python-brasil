# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num = int(input("Por favor, insira um valor (negativo ou positivo): "))

if num < 0:
    print(f"O número {num} é negativo!")
elif num > 0:
    print(f"O número {num} é positivo")
else:
    print("O número é igual a 0")