'''
Crie um programa que o usuário digita seu nome completo e mostre: 
a) O nome maiúsculo
b) O nome minúsculo
c) Quantidade de letras sem espaços
d) Quantas letras tem o primeiro nome
'''

nome = str(input('Digite seu nome completo: ')).strip()

print('Nome em maiúsculo: ',nome.upper())
print('Nome em minúsculo: ',nome.lower())
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))