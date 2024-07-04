#Escreva um programa que converta uma temperatura digitada em °C
#e converta para °F.

celcius = float(input('Informe a Temperatura em °C: '))

convercao = celcius * 9 / 5 + 32

print(f'A temperatura de {celcius:.1f}°C corresponde a {convercao:.1f}°F')

