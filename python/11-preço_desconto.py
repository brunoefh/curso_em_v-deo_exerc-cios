#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

produto = float(input('Informe o valor do produto: R$'))
desconto = produto * 0.95

print('O produto que custava R${:.2f} com o desconto custará R${:.2f}'.format(produto, desconto))
