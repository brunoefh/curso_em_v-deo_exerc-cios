#Faça um programa que escolha um número inteiro entre 1 e 5 e mostre na tela se o usuário acertou

import random

while True:
    numero = int(input('Escolha um número de 1 a 5: '))
    numero_aleatorio = random.randint(1, 5)
    if numero == numero_aleatorio:
        print('Você acertou')
        break;
    else:
        print('Você errou, o número verdadeiro era {}'.format(numero_aleatorio))