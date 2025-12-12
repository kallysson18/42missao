#!/usr/bin/env python3 
"""
Modifique seu programa anterior para remover duplicatas na saída. Você não deve
remover explicitamente valores de seus arrays.
Para este exercício, o uso de Set é obrigatório.
Por exemplo, se seu array original for [2, 8, 9, 48, 8, 22, -12, 2], a saída
deve ser semelhante a esta:
"""
num = [2, 8, 9, 48, 8, 22, -12, 2]

novo_array = set([n + 2 for n in num if n > 5])

print(num)
print(novo_array)
