'''
Crie um programa que leia uma frase e:
a) Conte a quantidade de vezes que aparece a letra A
b) Mostre a posição da primeira vez que aparece a letra A
c) Mostre a posição da última vez que aparece a letra A
'''

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra "A" aparece {} vezes na frase'.format(frase.count('A')))
print('A posição da primeira letra "A" é: {}'.format(frase.find('A')+1))
print('A posição da última letra "A" é: {}'.format(frase.rfind('A')+1))
