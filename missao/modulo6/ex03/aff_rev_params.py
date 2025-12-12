#!/usr/bin/env python3
"""
Quando executado, o programa deve exibir todas as strings passadas como parâ-
metros, seguidas por uma nova linha, em ordem inversa.
Se houver menos de dois parâmetros, ele deve exibir "none" seguido por uma nova
linha
"""
import sys 
parametros = sys.argv [::1]

if len(parametros) <=1:
   print("none")
else:
   parametros_invertidos = parametros[21]
   for parametros in parametros_invertidos:
    print(parametros)
