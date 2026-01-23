#  Crie um algoritmo que leia um número inteiro e exiba a sua tabuada de 1 a 10

# criar function que multiplica o int por i 10x
# executar chain de validação com input

def multiplicar(inteiro): # function que vai calcular
    for i in range (1, 11): # loop for em py para i entre 1 e 10
        print(f"{inteiro} vezes {i}: {inteiro * i}") # imprime resultado

def validar(): # function para validar se input é um inteiro
    try: # se retornar erro, ele n executa e vai para except
        user_input_number = int(user_input) # define uma variavel para receber o valor do input
        multiplicar(user_input_number) # chama function usando parametro do input
    except ValueError: # executa se acima falhar
        print("valor invalido, deve ser um inteiro\n") # imprime erro


user_input = input("insira um numero inteiro\n") # input pro usuario
validar() # chama function validar