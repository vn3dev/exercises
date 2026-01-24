# valida o input e retorna data de hoje

from datetime import date
import sys # lib para usar exit

def validar_input():
    user_input=input("Insira a o objetivo e a data nesse modelo: aprender python:dia/mes/ano") # pede o input
    user_input=user_input.replace("/", ":") # troca todos as barras por ":" ja que o split so aceita 1 argumento pra dividir
    user_input=user_input.split(":") # separa aonde tem ":" -> passa a ser um array

    objetivo=user_input[0] # guarda a string do começo

    data_atual_dict={ # guarda os valores da data em um dictionary
        "dias": int(user_input[1]),
        "meses": int(user_input[2]),
        "anos": int(user_input[3])
    }

    try: # se algo der false aqui ele vai pra except
        data_atual=date(data_atual_dict["anos"], data_atual_dict["meses"], data_atual_dict["dias"]) # converte para a tipagem date
        if data_atual < date.today(): # testa se a data ainda n passou
            print("Ops, essa data ja passou!")
            sys.exit() # encerra o programa depois da mensagem de erro
    except ValueError: # caso tente um valor fora do range do date
        print("Data invalida, tente novamente!")
        sys.exit()

    return objetivo, data_atual # devolve array com 2 valores, uma string e um date