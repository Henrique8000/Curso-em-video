# Ler valor em metros e converter em centímetros e milímetros

v_metros = float(input('Uma distância em metros: '))
km = v_metros / 1000
hm = v_metros / 100
dam = v_metros / 10
dm = v_metros * 10
cent = v_metros * 100
mili = v_metros * 1000

print(f'A medida de {v_metros}m corresponde a \n{km}km \n{hm}hm \n{dam}dam')
print(f'{dm}dm \n{cent:.0f}cm \n{mili:.0f}mm ')

