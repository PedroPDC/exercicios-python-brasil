# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

temp_celsius = int(input("Informe uma temperatura em graus Fahrenheit: "))
fahrenheit = (temp_celsius * (9 / 5)) + 32
print(f"A temperatura {temp_celsius}°C representa {round(fahrenheit, 2)}°F")