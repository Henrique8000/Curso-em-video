"""
Crie um programa que leia um número inteiro
na tela e mostre na tela se ele é PAR ou IMPAR
"""
from time import sleep


def main():
    n = int(input("Digite um número qualquer: "))
    p_ou_i(n)
    delay()


def p_ou_i(n):
    while n >= 0:
        if n % 2 == 1:
            print(f"\nO número {n} é ÍMPAR")

        else:
            print(f"\nO número {n} é PAR")

        n = int(input("\nDigite um número qualquer: "))


def delay():
    for i in range(3):
        if i == 0:
            print("Finalizando...")

        else:
            sleep(1.0)
            print("...")


main()
