# Faça um Programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é 
# vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. 
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

tamanho_area = float(input("Por favor, informe o tamanho em METROS QUADRADOS da área a ser pintada: "))

litros_necessarios = (tamanho_area / 6) * 1.1
if int(litros_necessarios) != litros_necessarios:
    litros_necessarios = int(litros_necessarios) + 1

capacidade_lata = 18
preco_lata = 80.00
capacidade_galao = 3.6
preco_galao = 25.00

latas_necessarias = litros_necessarios // capacidade_lata
if litros_necessarios % capacidade_lata > 0:
    latas_necessarias += 1
custo_latas = latas_necessarias * preco_lata

galoes_necessarios = litros_necessarios // capacidade_galao
if litros_necessarios % capacidade_galao > 0:
    galoes_necessarios += 1
custo_galoes = galoes_necessarios * preco_galao

latas_mistura = litros_necessarios // capacidade_lata
sobra_tinta = litros_necessarios % capacidade_lata
galoes_mistura = sobra_tinta // capacidade_galao
if sobra_tinta % capacidade_galao > 0:
    galoes_mistura += 1
custo_mistura = (latas_mistura * preco_lata) + (galoes_mistura * preco_galao)

print(f"\nApenas latas de 18 litros: {int(latas_necessarias)} lata(s), custo total: R$ {custo_latas:.2f}")
print(f"Apenas galões de 3,6 litros: {int(galoes_necessarios)} galão(ões), custo total: R$ {custo_galoes:.2f}")
print(f"Mistura de latas e galões: {int(latas_mistura)} lata(s) e {int(galoes_mistura)} galão(ões), custo total: R$ {custo_mistura:.2f}")