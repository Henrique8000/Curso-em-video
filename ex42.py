"""
Refaça o Desafio 035 dos triângulos, acrescentando o recurso de
mostrar que tipo de triângulo será formado:
-Equilátero: todos os lados iguais
-Isósceles: dois lados iguais
-Escaleno: todos os lados diferentes
"""



def main():
    nome_do_programa()
    lista_lados = entrada_3_lados_()
    existe_triangulo = condicao_de_existencia_triangulo(lista_lados)
    print(tipo_do_triangulo(existe_triangulo, lista_lados))


def entrada_3_lados_():
    l1 = float(input("Primeiro segmento: "))
    l2 = float(input("Segundo segmento: "))
    l3 = float(input("Terceiro segmento: "))
    l_segmentos = [l1, l2, l3]

    return l_segmentos


def condicao_de_existencia_triangulo(l_lados):
    existe = False
    if l_lados[0] < l_lados[1] + l_lados[2] and l_lados[1] < l_lados[2] + l_lados[0] and l_lados[2] < l_lados[1] + l_lados[0]:
        print("Os segmentos acima PODEM FORMAR um triângulo", end=" ")
        existe = True
        return existe

    else:
        print("Os segmentos acima NÃO PODEM FORMAR um triângulo", end=" ")
        return existe


def tipo_do_triangulo(existe, lados):
    if existe == True:

        if lados[0] == lados[1] == lados[2]:
            return 'EQUILÁTERO!'

        elif lados[0] != lados[1] != lados[2] != lados[0]:
            return 'ESCALENO!'

        else:
            return 'ISÓSCELES!'

    else:
        return '!'


def nome_do_programa():
    print("-=" * 20)
    print("Analizador de Triângulos")
    print("-=" * 20)


main()
