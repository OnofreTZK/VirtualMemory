from .global_var import *

# exit method
import sys

def processing_args( lista, filename, page_size, memory_size, PRA ) :
    "Processing arguments"
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

    if int(lista[4]) >= 128 and int(lista[4]) <= 16384 :
        memory_size = lista[4]
    else :
        print("O tamanho da memória disponível deve ser entre 128kb e 16384kB\n")
        sys.exit(1)

    # Returning a tuple.
    return ( filename, page_size, memory_size, PRA )
