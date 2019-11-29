
class Memory(object) :

#------------------------------------------------------------------------------------------------#

    def __init__( self, size, page_size, ALGORITHM ): #{{{
        self.space = [] * int(size) # memory size
        self.page = page_size # page size
        self.replc_algo = ALGORITHM # Chosen replacement algorithm
        self.Wop =0 # write operations count
        self.Rop =0 # read operations count
    #}}}


#------------------------------------------------------------------------------------------------#
    def parser( self, filepath ): #{{{
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
                self.Wop = self.Wop + 1
            else:
                self.Rop = self.Rop + 1


        return adresses
    #}}}

