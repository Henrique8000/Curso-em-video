"""
Faça um programa que leia três números e
mostre qual é o maior e qual é o menor.
"""


def main():
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())

    maior = 0
    menor = 0

    mn = verifica_menor(n1, n2, n3, menor)
    mor = verifca_maior(n1, n2, n3, maior)

    exibe_msg(mn, mor)


def verifica_menor(n1, n2, n3, menor):

    if n1 < n2 and n1 < n3:
        menor = n1

    elif n2 < n1 and n2 < n3:
        menor = n2

    else:
        menor = n3

    return menor


def verifca_maior(n1, n2, n3, maior):
    if n1 > n2 and n1 > n3:
        maior = n1

    elif n2 > n1 and n2 > n3:
        maior = n2

    else:
        maior = n3

    return maior


def exibe_msg(menor, maior):
    print(f"O menor valor digitado foi {menor}")
    print(f"O maior valor digitado foi {maior}")


main()