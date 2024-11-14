"""
Escreva um programa que faça o computador "pensar" em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu
"""

from random import randint
from time import sleep


numero = randint(0, 5)  #Faz o computador sortear um número entre 0 e 5

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' * 20)

n_usuario = int(input("Entre 0 e 5, qual número você acha que o computador escolheu? "))  #Usuário entra com um número inteiro entre 0 e 5

print("Processando...")
sleep(3)

if n_usuario == numero:  #Se o numero do usuário tiver o mesmo valor do numero do computador, ele irá exibir a mensagem a baixo
    print(f"Parabéns, você acertou! O número escolhido era {numero}")

else:  #Se o numero do usuário for diferente, então será exibida outra mensagem
    print("Puts, você errou o número :(")
