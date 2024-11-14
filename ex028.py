"""
Escreva um programa que faça o computador "pensar" em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu
"""

from random import randint

numero = randint(0, 5)

n_usuario = int(input("Entre 0 e 5, qual número você acha que o computador escolheu? "))

if n_usuario == numero:
    print(f"Parabéns, você acertou! O número escolhido era {numero}")

else:
    print("Puts, você errou o número :(")



