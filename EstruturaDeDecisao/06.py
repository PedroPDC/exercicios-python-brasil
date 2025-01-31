# Faça um Programa que leia três números e mostre o maior deles.

a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))
c = int(input("Digite o terceiro numero: "))

maior = a

if b > maior:
    maior = b
if c > maior:
    maior = c

print(f"O maior número é: {maior}")