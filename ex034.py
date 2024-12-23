"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00 calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%
"""


def main():
    salario = float(input("Qual é o salário do funcionário? R$"))
    lista_valores = novo_salario(salario)
    exibe_aumento_e_salario(lista_valores)


def novo_salario(salario):
    aumento = 0.00
    if salario <= 1250.00:
        aumento = (salario * 15 / 100) + salario

    else:
        aumento = (salario * 10 / 100) + salario

    lista_s_a = [salario, aumento]
    return lista_s_a


def exibe_aumento_e_salario(lista):
    print(f"Quem ganhava R${lista[0]:.2f} passa a ganhar R${lista[1]:.2f} agora.")


main()
