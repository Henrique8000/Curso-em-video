"""
Desenvolva um programa que leia o comprimento
de três retas e diga ao usuário se elas podem ou
não formar um triângulo.
"""


def main():
    nome_do_programa()
    lista_lados = entrada_3_lados_()
    condicao_de_existencia_triangulo(lista_lados)


def entrada_3_lados_():
    l1 = float(input("Primeiro segmento: "))
    l2 = float(input("Segundo segmento: "))
    l3 = float(input("Terceiro segmento: "))
    l_segmentos = [l1, l2, l3]

    return l_segmentos


def condicao_de_existencia_triangulo(l_lados):
    if l_lados[0] < l_lados[1] + l_lados[2] and l_lados[1] < l_lados[2] + l_lados[0] and l_lados[2] < l_lados[1] + l_lados[0]:
        print("Os segmentos acima PODEM FORMAR um triângulo!")

    else:
        print("Os segmentos acima NÃO PODEM FORMAR um triângulo!")


def nome_do_programa():
    print("-=" * 20)
    print("Analizador de Triângulos")
    print("-=" * 20)


main()
