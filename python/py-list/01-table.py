#  Crie um algoritmo que leia um número inteiro e exiba a sua tabuada de 1 a 10

# criar function que multiplica o int por i 10x
# executar chain de validação com input

def multiplicar(inteiro):
    for i in range (1, 11):
        print(f"{inteiro} vezes {i}: {inteiro * i}")

def validar():
    try:
        user_input_number = int(user_input)
        multiplicar(user_input_number)
    except ValueError:
        print("valor invalido, deve ser um inteiro\n")


user_input = input("insira um numero inteiro\n")
validar()