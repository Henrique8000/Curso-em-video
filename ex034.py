"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00 calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%
"""

salario = float(input("Qual é o salário do funcionário? R$"))
aumento = 0.00

if salario <= 1250.00:
    aumento = (salario * 15 / 100) + salario

else:
    aumento = (salario * 10 / 100) + salario

print(f"Quem ganhava R${salario:.2f} passa a ganhar R${aumento:.2f} agora.")
