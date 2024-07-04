# Ler quanto dinheiro há na carteira e mostrar quantos dólares e euros ela pode comprar
print('=====CÂMBIO=====')

carteira = float(input('Quanto dinherio você tem na carteira? R$'))

conver_dolar = carteira / 4.93

conver_euro = carteira / 5.30

print(f'\nPela cotação atual, com R${carteira:.2f} você pode comprar: U${conver_dolar:.2f}')
print(f'e {conver_euro:.2f}EUR')


