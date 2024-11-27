"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo
que ele foi multado. A multa vai custar R$7,00 por cada
Km acima do limite.
"""

velo_carro = int(input("Qual é a velocidade atual do carro? "))

if velo_carro <= 80 and velo_carro >= 0:
    print("Tenha um bom dia! Dirija com segurança!")

else:
    multa = (velo_carro - 80) * 7.00
    print("MULTADO! Você excedeu o limite permitido que é de 80Km/h")
    print(f"Você deve pagar uma multa de R${multa:.2f}!")
    print("Tenha um bom dia! Dirija com segurança!")
