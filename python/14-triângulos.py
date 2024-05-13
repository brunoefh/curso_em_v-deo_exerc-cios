'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
calcule e mostre o comprimento da hipotenusa
'''
import math
cateto_oposto = float(input('Informe o valor do cateto oposto: '))
cateto_adjacente = float(input('Informe o valor do cateto adjacente: '))
hipotenusa = math.hypot(cateto_adjacente, cateto_oposto)
print('O valor da hipotenusa é: {:.2f}' .format(hipotenusa))
