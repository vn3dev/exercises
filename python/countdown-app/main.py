# fazer um programa que receba um input "objetivo:data" - "aprender python:02/03/2026" e transformar isso em um countdown de dias
# ate esse objetivo. (Time remaining for your goal: learn python is X days)

from datetime import date # importa a lib

user_input=input("Insira a o objetivo e a data nesse modelo: aprender python:dia/mes/ano") # pede o input
user_input=user_input.replace("/", ":") # troca todos as barras por ":" ja que o split so aceita 1 argumento pra dividir
user_input=user_input.split(":") # separa aonde tem ":" -> passa a ser um array

objetivo=user_input[0] # guarda a string do começo

data_atual_dict={ # guarda os valores da data em um dictionary
    "dias": int(user_input[1]),
    "meses": int(user_input[2]),
    "anos": int(user_input[3])
}

data_atual=date(data_atual_dict["anos"], data_atual_dict["meses"], data_atual_dict["dias"]) # converte para a tipagem date
data_hoje=date.today() # guarda a data de hoje que ja vem no formato date
data_calculada=data_atual-data_hoje # calcula a diferenca
print(f"Tempo restante para seu objetivo: {objetivo} eh {data_calculada.days} dias") # imprime o output