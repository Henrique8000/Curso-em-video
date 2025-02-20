"""
A confederação nacional de natação precisa de um programa que
leia o ano de nascimento de um atleta e mostre sua categoria, de
acordo com a idade:
-Até 9 anos: MIRIM	-Até 19 anos: JUNIOR	Acima: MASTER
-Até 14 anos: INFANTIL 	-Até 25 anos: SÊNIOR
"""
from datetime import date


def main():

    ano = int(input("Ano de nascimento: "))
    idade_atleta = qnts_anos(ano)
    print(f"O atleta tem {idade_atleta} anos.")
    qual_classificacao(idade_atleta)


def qnts_anos(ano):

    return date.today().year - ano


def qual_classificacao(idade):

    if idade <= 9:
        print("Classificação: MIRIM")

    elif idade <= 14:
        print("Classificação: INFANTIL")

    elif idade <= 19:
        print("Classificação: JUNIOR")

    elif idade <= 25:
        print("Classificação: SÊNIOR")

    else:
        print("Classificação: MASTER")


main()
