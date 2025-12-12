#!/usr/bin/env python3
"""
Modifique seu programa anterior para processar apenas os valores maiores que 5 no
array original.
Por exemplo, se seu array original for [2, 8, 9, 48, 8, 22, -12, 2], a saída
deve ser
"""
num = [2, 8, 9, 48, 8, 22, -12, 2]

novo_array = []

for n in num:
    if n > 5:
        novo_array.append(n + 2)
    

print(num)
print(novo_array)