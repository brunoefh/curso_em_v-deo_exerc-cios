#Crie um programa que leia nomes e verifique se contem o nome ou sobrenome 'Silva'

nome = str(input('Digite seu nome comepleto: ')).strip()

aux = nome.upper() in 'SILVA'

print('O seu nome tem Silva? {}'.format(aux))
