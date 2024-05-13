#Faça um programa que leia o nome completo de um usuário e mostre o primeiro e último nome 

nome = input('Digite seu nome: ').strip().split()

print('Nome: {} \nSobrenome: {}'.format(nome[0], nome[-1]))
