# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

altura = float(input("Por favor, digite a sua altura em metros: "))
genero = input("Por favor, digite M para masculino e F para feminino: ")
peso_ideal_masc = (72.7 * altura) - 58
peso_ideal_fem = (62.1 * altura) - 44.7

if genero.upper() == "M":
    print(f"O peso ideal de uma pessoa de {altura} m é igual a: {round(peso_ideal_masc, 2)} kgs")
elif genero.upper() == "F":
    print(f"O peso ideal de uma pessoa de {altura} m é igual a: {round(peso_ideal_fem, 2)} kgs")
else:
    print("Por favor, insira os dados corretamente.")