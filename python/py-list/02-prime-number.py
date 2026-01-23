# Escreva um algoritmo que leia um número inteiro positivo e determine se ele é um número primo

def ehprimo(inteiro): # function do calculo
    for i in range(2, inteiro): # for entre 2 e inteiro -1
        if inteiro % i == 0: # testa se o valor eh divisivel por algum valor que n seja 1 ou ele mesmo
            print(f"{inteiro} eh divisivel por {i}, entao n eh primo") # output se if for true
            return # sai da function
    print("eh primo") # se ainda nao saiu da function quer dizer q todos os ifs sao falsos, logo eh primo

def validar(): # validacao para impedir input errado
    try: # garante que seja um inteiro positivo
        user_input_number = int(user_input)
        if user_input_number > 0:
            ehprimo(user_input_number)
        elif user_input_number == 0:
            print("valor invalido, deve ser um inteiro positivo\n")
    except ValueError:
        print("valor invalido, deve ser um inteiro positivo\n")

user_input=input("insira um numero inteiro positivo\n")
validar()
    
