#Crie um programa que o usuário digite "algo" e mostre seu tipo primitivo com todas as informações (is)

algo = input('Digite qualquer caractere:')

resultado = (
    f"{algo} é composto apenas por espaços? {algo.isspace()}\n"
    f"{algo} é composto apenas por dígitos ou letras? {algo.isalnum()}\n"
    f"{algo} é composto apenas por letras? {algo.isalpha()}\n"
    f"{algo} é composto apenas por dígitos? {algo.isdigit()}\n"
    f"{algo} é composto apenas por caracteres minúsculos? {algo.islower()}\n"
    f"{algo} é composto apenas por caracteres maiúsculos? {algo.isupper()}\n"
    f"{algo} é um identificador válido? {algo.isidentifier()}\n"
    f"{algo} é composto apenas por caracteres imprimíveis? {algo.isprintable()}"
)

print(resultado)