from datetime import date

user_input = input("Insira uma data:")
user_input = user_input.split("/")

dia = int(user_input[0])
mes = int(user_input[1])
ano = int(user_input[2])

data_alvo = date(ano, mes, dia)

data_hoje = date.today()

diferenca = data_alvo - data_hoje

print(f"Faltam {diferenca.days} dias")