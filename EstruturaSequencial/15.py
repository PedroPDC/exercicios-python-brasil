# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, 
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# a) salário bruto.
# b) quanto pagou ao INSS.
# c) quanto pagou ao sindicato.
# d) o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

salario_hora = float(input("Por favor, informe o seu salário por hora: R$"))
horas_trabalhadas = int(input("Por favor, insira o total de horas trabalhadas no mês: "))

salario_bruto = salario_hora * horas_trabalhadas
ir = salario_bruto * (11 / 100)
inss = salario_bruto * (8 / 100)
sindi = salario_bruto * (5 / 100)
descontos = ir + inss + sindi
salario_liquido = salario_bruto - descontos

print(
    f"\n+ Salário Bruto : R${salario_bruto}\n"
    f"- IR (11%) : R${ir}\n"
    f"- INSS (8%) : R${inss}\n"
    f"- Sindicato (5%) : R${sindi}\n"
    f"= Salário Liquido : R${salario_liquido}\n"
)
