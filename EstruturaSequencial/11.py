# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

a = int(input("Informe um primeiro número inteiro: "))
b = int(input("Informe um segundo número inteiro: "))
c = float(input("Informe um número real: "))

print(f"O produto do dobro do primeiro com metade do segundo é igual a: {(a * 2) * (b / 2)}")
print(f"A soma do triplo do primeiro com o terceiro é igual a: {(a * 3) + c}")
print(f"O terceiro elevado ao cubo é igual a: {c ** 3}")