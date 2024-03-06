#Crie um programa que leia 3 números e mostre qual é o maior e qual é o menor

a = float(input('Digite um número: '))
b = float(input('Digite outro número: '))
c = float(input('Digite mais um número: '))

if a > b and b > c and a > c:
    print(f'{a} é o maior e {c} é o menor número')
elif a > b and b < c and a > c:
    print(f'{a} é o maior e {b} é o menor número')
elif a > b and b < c and a < c:
    print(f'{c} é o maior e {b} é o menor número')
elif a < b and b < c and a < c:
    print(f'{c} é o maior e {a} é o menor número')
elif a < b and b > c and a > c:
    print(f'{b} é o maior e {c} é o menor número')
else:
    print(f'{b} é o maior e {a} é o menor número')
