# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. 
# A atribuição de conceitos obedece à tabela abaixo:
# Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” 
# se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

n1 = float(input("Por favor, insira sua primeira nota: "))
n2 = float(input("Por favor, insira sua segunda nota: "))

media = (n1 + n2) / 2

if media >= 9.0 and media <= 10.0:
    conceito = "A"
    status = "APROVADO"
elif media >= 7.5 and media < 9.0:
    conceito = "B"
    status = "APROVADO"
elif media >= 6.0 and media < 7.5:
    conceito = "C"
    status = "APROVADO"
elif media >= 4.0 and media < 6.0:
    conceito = "D"
    status = "REPROVADO"
elif media > 0 and media < 4.0:
    conceito = "E"
    status = "REPROVADO"
else:
    print("Insira um valor válido!")

print(f"\n1º Nota: {n1}")
print(f"2º Nota: {n2}")
print(f"Média: {round(media, 2)}")
print(f"Conceito: {conceito}")
print(f"Status: {status}")