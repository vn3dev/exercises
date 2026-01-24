# faz o calculo de dias restantes e retorna apenas o valor .days

from datetime import date

def calcular_dias(data_atual):
    resultado = (data_atual - date.today())
    return resultado.days