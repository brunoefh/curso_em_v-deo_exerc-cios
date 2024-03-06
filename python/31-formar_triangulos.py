#Crie um programa que leia 3 valores e diga se é possível formar um triangulo

a = float(input('Digite o primeiro lado de um triângulo: '))
b = float(input('Digite o segundo lado de um triângulo: '))
c = float(input('Digite o terceiro lado de um triângulo: '))

if a < b + c and b < a + c and c < a + b:
    print(f'É possível formar um triângulo com esses valores {a} {b} {c}')
else:
    print('Não é possível formar um triângulo com os valores informados')    
