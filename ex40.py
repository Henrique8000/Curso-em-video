"""
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
-Média abaixo de 5.0: REPROVADO
-Média entre 5.0 e 6.9: RECUPERAÇÃO
-Media 7.0 ou superior: APROVADO
"""


def main():
    notas = recebe_notas()
    meida_final = calcula_media(notas)
    aprovado_recuperacao_reprovado(notas, meida_final)


def recebe_notas():
    n1 = float(input("Primeira nota: "))
    n2 = float(input("Segunda nota: "))
    lista_notas = [n1, n2]
    return lista_notas


def calcula_media(notas):
    media = (notas[0] + notas[1]) / 2
    return media


def aprovado_recuperacao_reprovado(nota, media):
    if media >= 7.0:
        print(f"Tirando {nota[0]} e {nota[1]} a média do aluno é {media:.1f}\nO aluno está APROVADO")

    elif media >= 5.0:
        print(f"Tirando {nota[0]} e {nota[1]} a média do aluno é {media:.1f}\nO aluno está de RECUPERAÇÃO")

    else:
        print(f"Tirando {nota[0]} e {nota[1]} a média do aluno é {media:.1f}\nO aluno está REPROVADO")


main()
