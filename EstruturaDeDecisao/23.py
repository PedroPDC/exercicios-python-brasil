# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

numero = float(input("Digite um número qualquer: "))

if numero == round(numero):
    print(f"\nO número {numero} é INTEIRO.")
else:
    print(f"\nO número {numero} é DECIMAL.")