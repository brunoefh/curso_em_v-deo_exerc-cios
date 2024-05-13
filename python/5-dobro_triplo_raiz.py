#Crie um alogoritimo que informe um numero e mostre o dobro, o triplo e sua raiz quadrada

numero = float(input('Digite um número:'))
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = numero ** (1/2)

print('O número é: {} \nO dobro dele é: {} \nO triplo dele é: {} \nA raiz quadrada dele é: {}' .format(numero, dobro, triplo, raiz_quadrada))
