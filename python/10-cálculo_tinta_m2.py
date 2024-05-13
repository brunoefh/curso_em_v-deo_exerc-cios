'''
Faça um programa que leia a largura e altura de uma parede em metros, 
cálcule a sua área e a quantidade de tinta necessária para pintá-la, 
sabendo que cada litro de tinta pinta uma área de 2m²
'''

largura = float(input('Informe a largura:'))
altura = float(input('Informe a altura:'))
área = altura * largura
quantidade_tinta = área / 2 

print('A parede possuí uma área de {:.2f}m² e você precisará de {:.2f} litros de tinta para pintá-la completamente'.format(área, quantidade_tinta))
