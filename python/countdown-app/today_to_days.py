# puxa dados da lib datetime pra marcar o dia de hoje e converte tudo em dias
 
from datetime import date

days_today = date.today()
days_today_list = str(days_today).split("-") # faz a lita separando os elementos quando encontra "-"

date_today_dict = { # TAD pra separar dias meses e anos
    "days_today": int(days_today_list[2]),
    "months_today": int(days_today_list[1]),
    "years_today": int(days_today_list[0])
}

def total_days_today(): # puxa os dados do TAD e calcula tudo
    days = date_today_dict["days_today"]
    months = date_today_dict["months_today"]
    years = date_today_dict["years_today"]
    total_days = (days + (months * 30) + (years * 12 * 30))
    
    return(total_days) # retorna valor em dias totais desde o ano 0 da humanidade (código babilônico)