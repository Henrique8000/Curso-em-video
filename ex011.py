# Ler a largura e a altura de uma parede em metros, calcular a sua área e
# a quantidade de tinta necessária para pintá-la, sabendo que cada litro
# de tinta, pinta uma área de 2m²

v_largura = float(input('Largura da parede: '))
v_altura = float(input('Altura da parede: '))

a_parede = v_largura * v_altura
litro = a_parede / 2

print(f'Sua parede tem a dimensão de {v_largura:.1f}x{v_altura:.1f} e sua área é de {a_parede:.1f}m².', end=' ')
print(f'Para pintar essa parede você irá precisar de {litro:.1f}l de tinta')



