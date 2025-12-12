#!/usr/bin/env python3
"""O programa deve exibir o número de parâmetros passados para ele, seguido por
uma nova linha.
"""
import sys
num_parametros = len(sys.argv) - 1 
print(f"Número de parâmetros: {num_parametros}.")

