#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de
#um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
'''
#Sem módulo
cateto_oposto = float(input('Qual o tamanho do cateto oposto? '))
cateto_adjacente = float(input('Qual o tamanho do cateto adjacente? '))

hipo = ((cateto_oposto ** 2) + (cateto_adjacente ** 2)) ** (1/2)

print(f'O comprimento da Hipotenusa é igual a {hipo:.2f}')
'''

#Com módulo
from math import hypot

co = float(input('Insira o cateto oposto: '))
ca = float(input('Insira o cateto adjacente: '))

hi = hypot(co, ca)

print(f'O comprimento da hipotenusa é {hi:.2f}')
