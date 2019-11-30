from .global_var import *

## Python C-like struct s2 ##
from dataclasses import dataclass

# Queue for FIFO
import queue

# To save current time
from time import time

#---------------------------#
@dataclass
class PAGE: #{{{
    index: int# page index
    virtual_a: str # Adress
    time: float # Enter time
#}}}
#---------------------------#


class Memory(object) :

#------------------------------------------------------------------------------------------------#

    def __init__( self, size, page_size, ALGORITHM ): #{{{
        """ Memory Constructor """

        self.m_size = size
        self.page = page_size # page size
        self.ALGORITHM = ALGORITHM # Chosen replacement algorithm
        self.Wop =0 # write operations count
        self.Rop =0 # read operations count
        self.pg_fault =0 # page faults count
        self.slot_Space = int( int(size)/int(page_size) )

        # Selecting data structure according with replacement algorithm
        if ALGORITHM == PRA_LRU :
            self.slot = dict() * self.slot_Space # Dictionary to save time
        else:
            self.slot = [] * self.slot_Space  # Memory size
    #}}}


#------------------------------------------------------------------------------------------------#

    def parser( self, filepath ): #{{{
        """ Parsing file with adresses """

        self.filename = filepath

        # Opening file in read mode
        try:
            log_file = open( filepath, "r" )

        except IOError:
            print( "Não foi possível abrir o arquivo, certifique-se de fornecer o caminho certo!\n")
        virtual_adress = log_file.readlines() # saving all adresses and your op's

        adresses = [] * len(virtual_adress) # parse only the adress

        # Counting W's and R's
        for _line_ in virtual_adress :

            adresses.append(_line_.split()[0])

            if( _line_.split()[1].upper() == 'W' ):
                self.Wop += 1
            else:
                self.Rop += 1

        return adresses
    #}}}

#------------------------------------------------------------------------------------------------#

    def _search_in_virtual_( self, adress ): #{{{
        """ Search adress in memory slot """

        # Dictionary case
        # In this case the data is a struct page and key is time.
        if self.ALGORITHM == PRA_LRU :
            for _item_ in self.slot.items():
                if adress == _item_.virtual_a:
                    return True
        else: # List of dataclasses case
            for _adress_ in self.slot :
                if _adress_.virtual_a == adress :
                    return True

        # if loop has finished then the adress doesn't exist in memory
        # It's a page fault!
        self.pg_fault += 1

        return False
    #}}}

#------------------------------------------------------------------------------------------------#

    def FIFO( self, CACHE ): #{{{
        """ First In First Out replacement """

        # Queue of entrance
        first_order = queue.SimpleQueue()

        virtualIndex =0

        for i in range( len(CACHE) ):
            # controlling memory access
            if virtualIndex == self.slot_Space:
                if self._search_in_virtual_( CACHE[i] ) is not True :
                    # the adress doesn't exist in memory == page fault
                    # Put in memory in place of the first one entered in memory
                    first_out_page = first_order.get() # removing
                    self.slot[first_out_page.index] = PAGE( first_out_page.index, CACHE[i], time() )
                    # adding the page in fifo queue
                    first_order.put( self.slot[first_out_page.index] )
                else:
                    continue

            else: # Empty memory
                if self._search_in_virtual_( CACHE[i] ) is not True :
                    # the adress doesn't exist in memory == page fault
                    # Put in memory
                    self.slot.insert( virtualIndex,  PAGE( virtualIndex, CACHE[i], time() ) )
                    # adding the page in fifo queue
                    first_order.put( self.slot[virtualIndex] )
                    # increment memory index
                    virtualIndex += 1
                else:
                    continue

    #}}}

#------------------------------------------------------------------------------------------------#

    def simulate( self, CACHE ): #{{{
        """ Execute simulation """

        if self.ALGORITHM == PRA_FIFO:
            self.FIFO( CACHE )
        elif self.ALGORITHM == PRA_LRU:
            #not yet
            a
        else:
            b
            #not yet


    #}}}

#------------------------------------------------------------------------------------------------#

    def report( self ): #{{{
        """ Print data in terminal """

        print("""Arquivo de entrada {}\nTamanho da memória {} KB\nTamanho da página: {} KB
Tecnica de reposição: {}\nPáginas lidas: {}\nPáginas escritas: {}\nAcessos a memória: {}
Page faults: {}\n""".format( self.filename, self.m_size, self.page, self.ALGORITHM.upper(),
            self.Rop, self.Wop, 40, self.pg_fault ) )

        for slot in self.slot:
            print( slot )

   #}}}
