# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# a) par ou ímpar;
# b) positivo ou negativo;
# c) inteiro ou decimal.

def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

def verificar_positivo_ou_negativo(numero):
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "zero"
    
def verificar_inteiro_ou_decimal(numero):
    if numero == int(numero):
        return "inteiro"
    else:
        return "decimal"

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

operacao = input("Escolha a operação (+, -, *, /): ")

if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        print("Erro! Não é possível dividir por zero.")
        exit()
else:
    print("Operação Inválida")
    exit()

print(f"Resultado: {resultado}")

print(f"O resultado é {verificar_par_ou_impar(resultado)}, {verificar_positivo_ou_negativo(resultado)} e {verificar_inteiro_ou_decimal(resultado)}.")