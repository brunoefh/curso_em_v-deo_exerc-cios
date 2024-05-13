#Crie um programa que leia o nome de uma cidade e verifique se ela começa com a palavra "Santo"

cidade = str(input('Informe o nome de uma cidade: ')).strip()

print(cidade[:5].upper() == 'SANTO')
