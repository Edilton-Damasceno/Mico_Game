# *******************************
# Programa de teste do TAD Vector
# *******************************

import sys
import random
import math
from datetime import datetime

import cVetor

# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':

    if (len(sys.argv) > 1):
        n = int(sys.argv[1])
    else:
        n = 20

    v = cVetor.cVetor(n)
