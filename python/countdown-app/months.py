# receber parametros do input month, converter para dias e retornar valor calculado com base no date.today

# multiplica meses por 30 e retorna o valor, nem todos os meses tem 30 dias ent tem uma boa margem de imprecisão
def calculo_meses(date_dict):
    months = date_dict["months"]
    months = months * 30
    return (months)