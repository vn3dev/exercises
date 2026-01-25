# criar o menu interativo por CLI

import sys
sys.stdout.reconfigure(encoding="utf-8") # forca o uso de utf-8, git bash n estava conseguindo formatar o programa

def caixa_menu(titulo, opcoes, largura=50): # function para criar a caixa
    linha = "═" * largura # logica para "preencher" a largura da linha por "="
    print("╔" + linha + "╗") # linha do topo
    print("║" + titulo.center(largura) + "║") # centraliza o titulo entre uma quantidade de espaços = largura
    print("╠" + linha + "╣") # divisao para colocar as opções
    for opcao in opcoes: # opcao recebe um item da dict opcoes por iteracao
        print("║" + opcao.ljust(largura) + "║") # formata os itens a esquerda da linha "left justify"
    print("╚" + linha + "╝") # fecha a caixa


opcoes = [ # tad com a lista de opcoes, adicionar ou remover uma op nao quebra a formatacao da caixa_menu
    "1) Adicionar item",
    "2) Remover item",
    "3) Buscar item",
    "4) Listar estoque",
    "5) Total de itens",
    "0) Sair",
]
caixa_menu("PADARIA DO VANDERLEI", opcoes)