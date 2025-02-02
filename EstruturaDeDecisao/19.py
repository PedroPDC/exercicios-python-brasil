# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

num = int(input("Por favor, digite um numero menor que 1000: "))

if 0 <= num < 1000:
    centena = num // 100
    dezena = (num % 100) // 10
    unidade = num % 10

    resultado = f"\n{num} = "

    if centena > 0:
        resultado += f"{centena} {'centena' if centena == 1 else 'centenas'}"
        if dezena > 0 and unidade > 0:
            resultado += ", "
        elif dezena > 0 or unidade > 0:
            resultado += " e "

    if dezena > 0:
        resultado += f"{dezena} {'dezena' if dezena == 1 else 'dezenas'}"
        if unidade > 0:
            resultado += " e "
    
    if unidade > 0:
        resultado += f"{unidade} {'unidade' if unidade == 1 else 'unidades'}"

    print(resultado)

else:
    print("Número inválido! Digite um numero entre 0 e 999.")