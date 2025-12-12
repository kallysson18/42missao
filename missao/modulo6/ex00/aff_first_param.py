#!/usr/bin/env python3
"""
O programa deve exibir o primeiro parâmetro string passado, seguido por uma nova
linha.
Se não houver parâmetros, exiba "none"seguido por uma nova linha"""

import sys
if len(sys.argv) > 1:
   primeiro_parametro = sys.argv[1]
   print(primeiro_parametro)

else:
   print("none")