"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""


def main():
    ano = int(input("Ano de nascimento: "))
    idade = 2025 - ano

    print(f"\nQuem nasceu em {ano} tem {idade} anos em 2025")
    vai_p_alistamento(idade, ano)


def vai_p_alistamento(idade, ano):

    if idade == 18:
        print("Você tem que se alistar IMEDIATAMENTE!")

    elif idade < 18:
        print(f"Ainda faltam {18 - idade} anos para o alistamento.")
        print(f"Seu alistamento será em {ano + 18}.")

    else:
        print(f"Você já deveria ter se alistado há {idade - 18} anos.")
        print(f"Seu alistamento foi em {ano + 18}")


main()
