## Virtual Memory Simulator ##

# Authorship: Tiago Onofre & Pedro Nogueira.


#---------------------------- Imports and variables ---------------------------------#

# argv e argc
import sys

# all libraries used in this program
from libs import *

# file with virtual adresses and operation( read or write )
filepath = ''

# Page size in kilobytes( between 2kb and 64kb )
page_size =2

# Available memory size in kilobytes( between 128kb and 16384kb )
memory_size =128

# Page replacement algorithm name
PRA = ''

#------------------------------ Proccesing arguments --------------------------------#

# Unpacking the tuple in the right order.
filepath, page_size, memory_size, PRA = processing_args( sys.argv, filepath, page_size, memory_size, PRA )


# Vars are now ready do use
#-------------------------------- Reading data --------------------------------------#

# Memory object instantiation
CACHE = Memory( memory_size, memory_size, PRA )

adresses = CACHE.parser( filepath )

print(adresses)

