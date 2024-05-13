#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente

import math

angulo = int(input('Informe o ângulo: '))
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)
print('O ângulo é: {}° \nO seno é: {:.2f}° \nO cosseno é: {:.2f}° \nA tangente é: {:.2f}°' .format(angulo, seno, cosseno, tangente))
