# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

import math

a = int(input("Informe o valor de A: "))

if a != 0:
    b = int(input("Informe o valor de B: "))
    c = int(input("Informe o valor de C: "))
    delta = (b ** 2) - (4 * a * c)
    print(f"Delta: {delta}")
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"As raízes da equação são, x1: {x1} e x2: {x2}")
    elif delta == 0:
        x1 = -b / (2 * a)
        print(f"A raíz da equação é: {x1}")
    else:
        print("A equação nao possui raizes reais.")
else:
    print("A equação não é do segundo grau!")