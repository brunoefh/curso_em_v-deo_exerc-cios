#Escreva um programa que informe a quantidade de metros em centímetros e milímetros

metros = float(input('Digite a quantidade de metros:'))
centimetros = metros * 100
milimetros = metros * 1000

print('{} metros têm {} centímetros ou {} milímetros'.format(metros, centimetros, milimetros))
