"""
Faça um programa que leia uma frase pelo teclado e mostre:
-Quantas vezes aparece a letra "A"
-Em que posicao ela aparece a primeira vez
-Em que posicao ela aparece a ultima vez
"""

frase = str(input("Digite uma frase: ")).strip()

conta_letra = frase.upper().count('A')
acha_primeira_posicao = frase.replace('a', 'A').find('A')
acha_ultima_posicao = frase.lower().rfind('a')

print(f"A palavra 'A' aparece {conta_letra} vezes")
print(f"A primeira letra 'A' apareceu na posicao {acha_primeira_posicao}")
print(f"A ultima letra 'A' apareceu na posicao {acha_ultima_posicao}")
