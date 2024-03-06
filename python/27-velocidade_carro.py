#Escreva um programa que leia a velocidade de um carro, se ultrapassar o limite de 80km/h, mostre que foi multado e aplique uma multa de R$7,00 por cada km acima do limite

velocidade = int(input('Qual foi a velocidade máxima atingida em km por hora: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7 
    print('Você ultrapassou o limite de velocidade e terá que pagar uma multa de R${},00'.format(multa))
else:
    print('Você está dentro do limite de velocidade, dirija com segurança!')
