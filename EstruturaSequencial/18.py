# Faça um programa que peça o tamanho de um arquivo para download (em MB) e 
# a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho_arquivo = float(input("Por favor, informe o tamanho do arquivo a ser baixado (em MB): "))
velocidade_internet = float(input("Por favor, informe a velocidade de sua internet (em Mbps): "))
velocidade_mbps = velocidade_internet * 0.125

tempo = (tamanho_arquivo / velocidade_internet) / 60

print(f"Um arquivo de {tamanho_arquivo}Mb, demoraria aproximadamente {tempo}min para ser baixado em uma internet de {velocidade_mbps}Mbps")