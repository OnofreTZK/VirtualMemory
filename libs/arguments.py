from .global_var import *

# exit method
import sys

def processing_args( lista, filename, page_size, memory_size, PRA ) :
    "Processing arguments"

    if( len(lista) < 5 or len(lista) > 5 ):
        print("""Argumentos inválidos! Por favor informe na seguinte ordem:

\033[34m<algoritmo_de_substituição>:\033[0m
least recently used - 'lru'
full random = 'random'
first-in first-out - 'fifo'

\033[34m<arquivo_com_os_endereços>\033[0m: informe o caminho caso necessário
\033[34m<tamanho_da_pagina>\033[0m: entre 2kB e 64kB
\033[34m<tamanho_da_memória\033[0m: entre 128kB e 16384kB\n""")
        sys.exit(1)

    # Getting filename
    if '.log' in lista[2] or '.txt' in lista[2] :
        filename = lista[2]

    else:
        print("Forneça um arquivo válido!\n")
        sys.exit(1)

    #############################################################
    # Getting chosen algorithm #

    if lista[1].lower() == PRA_RAND :
        PRA = PRA_RAND

    elif lista[1].lower() == PRA_LRU :
        PRA = PRA_LRU

    elif lista[1].lower() == PRA_FIFO :
        PRA = PRA_FIFO

    else :
        print("""Escolha um algoritmo de substituição válido!
last recent used - 'lru'
full random = 'random'
first-in first-out - 'fifo'\n""")
        sys.exit(1)
    ##############################################################

    # Getting page size
    if int(lista[3]) >= 2 and int(lista[3]) <= 64 :
        page_size = int(lista[3])
    else :
        print("Por favor, informe um tamanho de página entre 2kB e 64kB\n")
        sys.exit(1)

     # Getting memory size   
    if int(lista[4]) >= 128 and int(lista[4]) <= 16384 :
        memory_size = lista[4]
    else :
        print("O tamanho da memória disponível deve ser entre 128kb e 16384kB\n")
        sys.exit(1)

    # Returning a tuple.
    return ( filename, page_size, memory_size, PRA )
