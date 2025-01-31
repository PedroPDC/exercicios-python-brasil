# Faça um Programa que leia três números e mostre o maior e o menor deles.

a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))
c = int(input("Digite o terceiro numero: "))

maior = a
menor = a

# Verifica maior
if b > maior:
    maior = b
if c > maior:
    maior = c

# Verifica menor
if b < menor:
    menor = b
if c < menor:
    menor = c

print(f"\nO maior número é: {maior}")
print(f"O menor número é: {menor}")