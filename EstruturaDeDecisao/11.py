# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que 
# calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario_atual = float(input("Por favor, informe seu salário atual: R$"))

if salario_atual <= 280.00:
    percent_aumento = 0.2
    valor_aumento = salario_atual * percent_aumento
    novo_salario = salario_atual + valor_aumento

elif salario_atual > 280.00 and salario_atual <= 700.00:
    percent_aumento = 0.15
    valor_aumento = salario_atual * percent_aumento
    novo_salario = salario_atual + valor_aumento

elif salario_atual > 700.00 and salario_atual <= 1500.00:
    percent_aumento = 0.1
    valor_aumento = salario_atual * percent_aumento
    novo_salario = salario_atual + valor_aumento

else:
    percent_aumento = 0.05
    valor_aumento = salario_atual * percent_aumento
    novo_salario = salario_atual + valor_aumento

print(f"\nSalário vigente: R${salario_atual}")
print(f"Percentual de aumento: {percent_aumento*100}%")
print(f"Valor do aumento: R${valor_aumento}")
print(f"Novo salário: R${novo_salario}")