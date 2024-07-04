#Faça um algoritmo que leia o salário de um funcionário e mostre
#seu novo salário, com 15% de aumento.

s_funcio = float(input('Qual é o salário do Funcionário? R$'))

novo_s = (s_funcio * 15 / 100) + s_funcio

print(f'Um funcionário que ganhava R${s_funcio:.2f}, com 15% de aumento, passa a receber R${novo_s:.2f}')
