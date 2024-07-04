# Ler número e mostrar na tela seu dobro, triplo e raiz quadrada
# Entrada de dados / declaração da váriavel "num" (número inteiro)
num = int(input('Digite um número: '))

# Váriáveis de processamento
# d = num * 2
# t = num * 3)
# r = num ** (1/2)
# fim = 'fim do programa!'

# Saída de dados
# print(f'O dobro de {num} é: {d}', end=', ')
# print(f'o triplo de {num} é: {t}', end=' e ')
# print(f'a raiz quadrada de {num} é: {r}')
# print(f'\n{fim.upper():=^40}')

print(f'O dobro de {num} vale {num * 2}.')
print(f'O triplo de {num} vale {num * 3} \nA raiz quadrada de {num} é igual a {num **(1/2):.2f}')


