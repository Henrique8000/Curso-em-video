#Faça um programa que leia um número inteiro qualquer e
#mostre na tela a sua tabuada.

numero = int(input("Digíte um número inteiro: "))
print(10 * '-')
#print(f"A tabuada do '{numero}' é:\n")
#print(f'{numero} x 0 = {numero*0}')
#print(f'{numero} x 1 = {numero*1}')
#print(f'{numero} x 2 = {numero*2}')
#print(f'{numero} x 3 = {numero*3}')
#print(f'{numero} x 4 = {numero*4}')
#print(f'{numero} x 5 = {numero*5}')
#print(f'{numero} x 6 = {numero*6}')
#print(f'{numero} x 7 = {numero*7}')
#print(f'{numero} x 8 = {numero*8}')
#print(f'{numero} x 9 = {numero*9}')
#print(f'{numero} x 10 = {numero*10}')

#Tabuada feita com laço de reptição 'for':
#i = 0  (não é necessário)

#for i in range(i, 11):
#    mult = i * numero
#    print(f'{numero} x {i} = {mult}')

#Tabuada feita com laço 'for' 2.0
for i in range(0, 11):
    print(f'{numero} x {i} = {i * numero}')

print(10 * '-')
print("\nFIM DO PROGRAMA!")
