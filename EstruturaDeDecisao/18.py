# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

data = input("digite uma data no formato dd/mm/aaaa: ")

def ano_bissexto(ano):
    return (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0))

if len(data) == 10 and data[2] == "/" and data[5] == "/":
    try:
        dia, mes, ano = map(int, data.split("/"))

        if mes < 1 or mes > 12:
            print("Data inválida!")
        elif dia < 1 or (mes in [1, 3, 5, 7, 8, 10, 12] and dia > 31):
            print("Data inválida!")
        elif mes in [4, 6, 9, 11] and dia > 30:
            print("Data inválida!")
        elif mes == 2 and dia > 28:
            if ano_bissexto(ano) and dia == 29:
                print("Data válida!")
            else:
                print("Data inválida!")
        else:
            print("Data válida!")
    except ValueError:
        print("Data inválida!")
else:
    print("Formato inválido!")