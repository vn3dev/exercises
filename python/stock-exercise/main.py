# Escreva um algoritmo que leia os preços de 10 produtos e suas quantidades em
# estoque. Calcule e mostre o total em estoque.

produtos=[] # define vars como vetor
quantidade=[]
MAX=3 # variavel pra alterar o range dos loops

for i in range(0, MAX): # loop para coletar os dados >>AUMENTAR RANGE<<
    user_input=input("Insira o produto numero {i} e a quantidade separados por /: \nEXEMPLO: veda rosca/30\n")
    user_input=user_input.split("/") # separa em array o input separado por /
    produtos.append(user_input[0]) # adiciona no array
    quantidade.append(int(user_input[1])) # adiciona no array mas primeiro converte para inteiro
    print(f"Adicionou {produtos[i]}, {quantidade} com sucesso") # confirmacao visual pro usuario

total=0 # define como inteiro e inicializa com 0
for i in range(0, MAX): # loop pra fazer o calculo
    total = total + quantidade[i]

print(total) # output final da quantidade de itens em estoque