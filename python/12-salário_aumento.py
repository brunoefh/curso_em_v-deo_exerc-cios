#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

salário = float(input('Informe o seu salário: '))
salário_atual = salário * 1.15

print('O seu novo salário é: R${:.2f}'.format(salário_atual))
