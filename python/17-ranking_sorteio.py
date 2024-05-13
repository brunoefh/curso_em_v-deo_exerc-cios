#Faça um programa que leia nomes e crie um ranking aleatório

import random
nome = ['Bruno', 'Daniel', 'Gabriel', 'Thales']
ranking = random.sample(nome, len(nome))
print('O ranking dos mais héteros: \n1°: {} \n2°: {} \n3°: {} \n4°: {}'.format(*ranking))
