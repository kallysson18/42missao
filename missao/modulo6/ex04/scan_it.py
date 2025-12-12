#!/usr/bin/env python3 
"""O primeiro parâmetro é uma palavra-chave para procurar em uma string.
O segundo parâmetro é a string a ser pesquisada.
Quando executado, o programa deve exibir o número de vezes que a palavra-chave
aparece na string.
Se o número de parâmetros for diferente de 2 ou se a primeira string não aparecer
na segunda, ele deve exibir none seguido por uma nova linha."""

import sys

parametro = sys.argv[1:]

if len(parametro) != 2:
    print("none")
    exit()

palavra = parametro[0]
texto = parametro[1]

contagem = texto.count(palavra)

if contagem == 0:
    print("none")
else:
    print(contagem)

