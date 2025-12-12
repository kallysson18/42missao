#!/usr/bin/env python3
""" O programa deve exibir a string em letras maiúsculas, seguida por uma nova linha.
Se o número de parâmetros for diferente de 1, exiba "none"seguido por uma nova
linha.
"""
import sys
if len(sys.argv) > 1:
   parametro = sys.argv[1]
   print(parametro.upper())
else:
   print("none") 