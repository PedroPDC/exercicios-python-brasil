# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

temp_fahrenheit = int(input("Informe uma temperatura em graus Fahrenheit: "))
celsius = 5 * ((temp_fahrenheit - 32) / 9)
print(f"A temperatura {temp_fahrenheit}°F representa {round(celsius, 2)}°C")