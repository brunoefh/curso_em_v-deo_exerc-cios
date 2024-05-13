'''
Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira
Ex: digite: 6.127
O número 6.127 tem a parte inteira 6
'''
import math
numero = float(input('Digite um número: '))
print('A parte inteira do número {} é {}'.format(numero, math.floor(numero)))
