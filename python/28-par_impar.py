#Crie um programa que identifique se um número inteiro é par ou ímpar

número = int(input('Digite um número inteiro: '))
resultado = número % 2
if resultado == 1:
    print(f'o número {número} é ímpar')
else:
    print(f'o número {número} é par')
    