##022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = input('Insira o seu nome completo:')

print(f'\nEm maiúsculas: {nome.upper()} .Em minúsculas: {nome.lower()}\n')

print(f'Quantidade de letras ao todo (sem o espaço): {len(nome.replace(" ", ""))}\n')

dividido = nome.split()
print(f'Quantidade de letras do primeiro nome: {len(dividido[0])}')
