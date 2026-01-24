# PIOR CODIGO JA FEITO DESDE A INVENCAO DA RODA, deve ter uma lib pra melhorar isso

# fazer um programa que receba um input "objetivo:data" - "aprender python:02/03/2026" e transformar isso em um countdown de dias
# ate esse objetivo. (Time remaining for your goal: learn python is X days)

# modularizar e criar logica input base
# multiplicar meses/anos para dias
# somar tudo e exibir para o usuario

from datetime import date # importa function para saber q dia eh hoje
from months import calculo_meses # importa functions dos outros arquivos .py
from today_to_days import total_days_today
from years import calculo_anos

user_input = input("Insira seu objetivo e data esperada para completar. Exemplo: aprender python:02/03/2026\n") # pede o input
user_input = user_input.replace("/", ":") # troca os caracteres "/" da string por ":"
objective_and_date = user_input.split(":") # converte em lista os itens da string separados por ":"

date_dict = { # dict para separar dias meses e anos
    "days": int(objective_and_date[1]),
    "months": int(objective_and_date[2]),
    "years": int(objective_and_date[3])
    
}
objective_and_date_dict = { # dict que nem precisava existir
    "objective": str(objective_and_date[0]),
}

# chama as functions e faz a soma do total de dias para o objetivo desde o ano 0
dias_final = (date_dict["days"] + calculo_meses(date_dict) + calculo_anos(date_dict))
# chama a function que calcula quantos dias existem hoje desde o ano 0 KKKKKK
dias_hoje = total_days_today()
# calcula a diferença
dias_calculado = (dias_final - dias_hoje)
# exibe o output final, de forma imprecisa ja que os meses são calculados sempre * 30
print(f"Time remaining for {objective_and_date_dict["objective"]} is {dias_calculado} days")