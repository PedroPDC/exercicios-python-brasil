# Faça um Programa que leia três números e mostre-os em ordem decrescente.

a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))
c = int(input("Digite o terceiro numero: "))

maior = a
menor = a
medio = a

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

# Verifica numero do meio
if b > menor and b < maior:
    medio = b
if c > menor and c < maior:
    medio = c

print(f"\n{maior}, {medio}, {menor}")