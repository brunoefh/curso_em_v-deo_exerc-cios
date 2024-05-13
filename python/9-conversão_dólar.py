#Crie um programa que faça a conversão de reais para dólares 06/02/24 (US$ 1,00 = R$ 4,97)

reais = float(input('Informe quantos reais quer converter: R$'))
dólar = 4.97
resultado = reais / dólar
print('Com R${:.2f} reais você pode comprar US${:.2f} dólares'.format(reais, resultado))
