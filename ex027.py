"""
Primeiro e ultimo nome de uma pessoa
"""

nome = str(input("Digite o seu nome completo: ")).strip()
n = nome.split()

print("Muito prazer em te conhecer!!!")
print(f"Seu primeiro nome é {n[0]}")
print(f"Seu ultimo nome é {n[-1]}")
