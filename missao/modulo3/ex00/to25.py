#!/usr/bin/env python3
"""Use um loop para exibir todos os números de um número inserido até 25.
◦ Se o número de entrada for maior que 25, exiba "Error"seguido por uma nova
linha.
"""
num = int(input("Digite um número: "))
if num > 25:
    print("Error\n")
else:
    while num <= 25:
        print(f"Dentro do loop, minha variável é {num}")
        num += 1