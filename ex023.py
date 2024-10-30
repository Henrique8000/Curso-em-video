#Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos dígitos separados
#Ex:
#Digite um número 1834
#unidade:4 dezena:3 centena:8 milhar:1

numero = int(input())

# tratamento de cadeia de caracteres
'''n = str(numero)

print(f"unidade: {n[3]}")
print(f"dezena: {n[2]}")
print(f"centena: {n[1]}")
print(f"milhar: {n[0]}")
'''

#forma matemática e mais adequada
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print(f"unidade: {u}")
print(f"dezema: {d}")
print(f"centena: {c}")
print(f"milhar: {m}")
