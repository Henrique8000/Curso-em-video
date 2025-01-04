'''
escreva um programa que leia um número inteiro qualquer e peça
para o usuário escolher qual será a base de conversão
'''


def main():
    main_menu = True
    while main_menu:
        opcao = menu_principal()

        if opcao[1] == '1':
            converte_p_binario(opcao[0])

        elif opcao[1] == '2':
            converte_p_octal(opcao[0])

        elif opcao[1] == '3':
            converte_p_hexa(opcao[0])

        elif opcao[1] == '4':
            print("Finalizando...")
            main_menu = False

        else:
            main_menu = trata_execao(opcao, main_menu)


def menu_principal():
    n = int(input("Digite um número inteiro: "))
    print("\nEscolha uma opção para conversão:")
    print("[ 1 ] converter para BINÁRIO")
    print("[ 2 ] converter para OCTAL")
    print("[ 3 ] converter para HEXADECIMAL")
    print("[ 4 ] Sair")
    op = input('Sua opção: ').strip()

    numero_e_opcao = [n, op]
    return numero_e_opcao


def converte_p_binario(n):
    print(f'{n} convertido para BINÁRIO é igual a {n:b}')


def converte_p_octal(n):
    print(f'{n} convertido para OCTAL é igual a {n:o}')


def converte_p_hexa(n):
    print(f'{n} convertido para HEXADECIMAL é igual a {n:x}')


def trata_execao(opcao, main_menu):
    entrada_errada = True

    while entrada_errada:
        opcao[1] = input("\nDigite uma opção válida!(1 - 4) ").strip()
        if opcao[1] == '1':
            converte_p_binario(opcao[0])
            entrada_errada = False

        elif opcao[1] == '2':
            converte_p_octal(opcao[0])
            entrada_errada = False

        elif opcao[1] == '3':
            converte_p_hexa(opcao[0])
            entrada_errada = False

        elif opcao[1] == '4':
            print('Finalizando...')
            main_menu = False
            break

    return main_menu


main()
