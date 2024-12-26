"""
Escreva um programa para aprovar o empréstimo bancário para a compra
de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos
anos ele vai pagar. A prestação mensal, não pode exceder 30% do salário ou
então o empréstimo será negado
"""

v_casa = float(input("Valor da casa: R$"))
v_salario = float(input("Salário do comprador: R$"))
v_financiamento = int(input("Quantos anos de financiamento? "))

prestacao_mensal = v_casa / (v_financiamento * 12)

cond_salario = v_salario * 30 / 100

print(f"\nPara pagar uma casa de R${v_casa:.2f} em {v_financiamento} anos a prestação será de R${prestacao_mensal:.2f}")

if prestacao_mensal > cond_salario:
    print("\033[31mEmpréstimo NEGADO!")

else:
    print("\033[32mEmpréstimo pode ser CONCEDIDO!")
