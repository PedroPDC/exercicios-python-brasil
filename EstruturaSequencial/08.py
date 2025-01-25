# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

salario_por_hora = float(input("Por favor, informe o quanto você ganha por hora R$"))
horas_trabalhadas = int(input("Informe quantas horas você trabalhou no mês: "))

salario = salario_por_hora * horas_trabalhadas

print(f"Seu salário no mês foi de R${salario}")