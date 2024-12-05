"""
Desenvolva um programa que pergunte a dustância de uma viagem
em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para
viagens de até 200Km e R$0,45 para viagens mais longas.
"""
total = 0.00
distancia = float(input("Qual é a distância da sua viagem? "))

if distancia <= 200.0:
    total = distancia * 0.50

else:
    total = distancia * 0.45

print(f"Você está prestes a começar uma viagem de {distancia:.2f}Km.")
print(f"E o preço da sua passagem será de R${total:.2f}")

