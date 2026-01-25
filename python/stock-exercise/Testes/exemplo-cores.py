PRETO   = "\033[30m"
VERMELHO= "\033[31m"
VERDE   = "\033[32m"
AMARELO = "\033[33m"
AZUL    = "\033[34m"
MAGENTA = "\033[35m"
CIANO   = "\033[36m"
BRANCO  = "\033[37m"
PRETO_C   = "\033[90m"
VERMELHO_C= "\033[91m"
VERDE_C   = "\033[92m"
AMARELO_C = "\033[93m"
AZUL_C    = "\033[94m"
MAGENTA_C = "\033[95m"
CIANO_C   = "\033[96m"
BRANCO_C  = "\033[97m"
RESET      = "\033[0m"
NEGRITO    = "\033[1m"
DIM        = "\033[2m"
ITALICO    = "\033[3m"   # nem todo terminal suporta
SUBLINHADO = "\033[4m"
PISCAR     = "\033[5m"   # raramente suportado
REVERSO    = "\033[7m"
OCULTO     = "\033[8m"


print(NEGRITO + MAGENTA + "teste blablabla" + RESET)
print(VERDE + "1) Adicionar item" + RESET)