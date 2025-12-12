#!/usr/bin/env python3
"""O programa recebe uma string como parâmetro.
Ele deve exibir a string em letras minúsculas, seguida por uma nova linha.
Se o número de parâmetros for diferente de 1, ele deve exibir "none"seguido por
uma nova linha."""

import sys

if len(sys.argv) > 1:
    parametro = sys.argv[1]
    print(parametro.lower())
else:
    print("none")