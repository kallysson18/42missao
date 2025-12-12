#!/usr/bin/env python3
"""Quando executado, o programa deve solicitar que o usuário insira 2 números.
Exibir se o resultado da multiplicação dos dois números é positivo, negativo
ou zero.
 Exibir o resultado da multiplicação.
"""


first_number = float(input("Insira o primeiro numero:\n"))
second_number = float(input("Insira o segundo numero:\n"))
resultado = first_number * second_number
print(f"{first_number} * {second_number} = {resultado}")
if resultado > 0:
    print("O resultado é positivo.")
elif resultado < 0:
    print("O resultado é negativo.")
else:
    print("O resultado é positivo e negativo.")
 
