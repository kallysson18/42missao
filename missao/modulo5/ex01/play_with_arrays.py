#!/usr/bin/env python3
"""
Defina um array de números.
Itere sobre este array, criando um novo array adicionando 2 a cada valor no array
original.
Seu programa deve conter dois arrays: o array original e o array modificado.
Exiba ambos os arrays na tela.
"""
num = [2, 8, 9, 48, 8, 22, -12, 2]

novo_array = []

for n in num:
    novo_array.append(n + 2)

print("Original array: ", num)
print("New array:", novo_array)
