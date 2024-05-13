#Faça um programa que leia um número inteiro e imprima o seu sucessor e antecessor

numero = int(input('Digite um número inteiro:'))
antecessor = numero - 1
sucessor = numero + 1

print('O número é: {} \nSeu antecessor é: {} \nSeu sucessor é: {}' .format(numero, antecessor, sucessor))
