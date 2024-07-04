#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
#Ex: Digite um número: 6.127
#O número 6.127 tem a
#parte Inteira 6.
#import math
from math import trunc

num = float(input('Digite um número: '))

#a = math.floor(num)

print(f'O número {num} tem a parte Inteira {trunc(num)}')


'''
num = float(input('Digite um número: '))
converte = int(num)
print(f'O valor {num} tem como sua forma inteira {converte}')
'''