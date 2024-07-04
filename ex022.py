##022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = input('Insira o seu nome completo:')

print(f'Em maiúsculas: {nome.upper()}.Em minúsculas: {nome.lower()}')

print(len(nome.replace(' ', '')))

dividido = nome.split()
print(len(dividido[0]))
'''for i in dividido:
    print(len(i), i)'''
