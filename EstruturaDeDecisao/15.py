# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

a = float(input("Por favor, insira o primeiro lado do triângulo: "))
b = float(input("Por favor, insira o segundo lado do triângulo: "))
c = float(input("Por favor, insira o terceiro lado do triângulo: "))

if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print("\nTriângulo Equilátero")
    elif a == b or b == c or c == a:
        print("\nTriângulo Isósceles")
    else:
        print("\nTriângulo Escaleno")
else:
    print("\nOs valores informados não formam um triângulo")