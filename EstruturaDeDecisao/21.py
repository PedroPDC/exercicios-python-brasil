# Faça um Programa para um caixa eletrônico. 
# O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

saque = int(input("Por favor, insira o valor que deseja sacar: [Mínimo R$10 e máximo R$600]: R$"))

if saque < 10 or saque > 600:
    print("Valor inválido. O valor mínimo é R$10 e o máximo é R$600.")
else:
    notas_100 = saque // 100
    saque %= 100

    notas_50 = saque // 50
    saque %= 50

    notas_10 = saque // 10
    saque %= 10

    notas_5 = saque // 5
    saque %= 5

    notas_1 = saque

    print(f"\n{notas_100} nota(s) de 100 reais."
          f"\n{notas_50} nota(s) de 50 reais"
          f"\n{notas_10} nota(s) de 10 reais"
          f"\n{notas_5} nota(s) de 5 reais"
          f"\n{notas_1} nota(s) de 1 real")


