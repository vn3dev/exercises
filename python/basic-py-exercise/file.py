link = "https://web.whatsapp.com/"
grupo = "Empresa"
mensagem = "Bom dia"

# Passo 1: Abrir o menu iniciar
# Passo 2: Abrir o navegador
# Passo 3: Acessar o site da Kabum
# Passo 4: Pesquisar pelo produto
# Passo 5: Clicar em pesquisar

import pyautogui
import time

# pyautogui.write("chroma") -> digita algo
# pyautogui.click() -> clica em alguma posição a tela
# pyautogui.press("enter") -> pressiona uma tecla
# pyautogui.hotkey("win", "s") -> atalho de teclado

pyautogui.PAUSE = 0.5

pyautogui.press("win") # abre menu iniciar
pyautogui.write("brave") # digita o nome do navegador
pyautogui.press("enter") # pressiona enter para abrir o navegador

pyautogui.write(link) # escreve o link no endereçador
pyautogui.press("enter") # acessa o endereço
time.sleep(8) # espera 8 secs para carregar

pyautogui.click(x=244, y=163) # clica na pesquisa de conversa

pyautogui.write(grupo) # escreve o nome do grupo
time.sleep(2) # espera 2 secs

pyautogui.click(x=261, y=349) # clica no primeiro grupo correspondente
pyautogui.write(mensagem) # escreve a mensagem
pyautogui.press("enter") # envia

# usar task scheduler para setar mensagem de bom dia grupo <3