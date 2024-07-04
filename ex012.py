#Faça um algoritmo que leia o preço do produto e mostre seu
#novo preço, com 5% de desconto
preco = float(input('Qual é o preço do produto? R$'))

desconto = preco - (preco * 30 / 100)

print(f'O produto que custava R${preco}, na promoção com desconto de 5% vai custar R${desconto:.2f}')
