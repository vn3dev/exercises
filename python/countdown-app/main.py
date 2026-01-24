# fazer um programa que receba um input "objetivo:data" - "aprender python:02/03/2026" e transformar isso em um countdown de dias
# ate esse objetivo. (Time remaining for your goal: learn python is X days)

from validar_input import validar_input
from calcular_dias import calcular_dias

validado=validar_input()
string_objetivo=(validado[0])
data_atual=(validado[1])
resultado_dias=calcular_dias(data_atual)

print(f"Tempo restante para seu objetivo: {string_objetivo} eh {resultado_dias} dias") # imprime o output