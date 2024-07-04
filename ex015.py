#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

pago = (dias * 60) + (km * 0.15)
mes = pago / 12

print(f'\nO aluguel fica R${pago:.2f}\n')

print(f'Parcelando em 12X sem juros, você pagará R${mes:.2f} por mês.')


