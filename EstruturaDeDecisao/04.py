# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

vogais = ["A", "E", "I", "O", "U"]

letra = input("Digite uma letra: ").upper()

if letra.isalpha() and len(letra) == 1:
    if letra in vogais:
        print(f"A letra {letra} é uma vogal.")
    else:
        print(f"A letra {letra} é uma consoante.")
else:
    print("Entrada inválida! Digite apenas uma única letra")