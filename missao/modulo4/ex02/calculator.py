#!/usr/bin/env python3
try:
    n1 = float(input("Me dê o primeiro número: "))
    n2 = float(input("Me dê o segundo número: "))
except ValueError:
    print("Insira um número válido")
    exit(1)
    
print("Obrigado!")
print(f"{n1} + {n2} = {n1 + n2}")
print(f"{n1} - {n2} = {n1 - n2}")

if n2 != 0:
    print(f"{n1} / {n2} = {n1 / n2}")
else:
    print(f"{n1} / {n2} = Erro: Divisão por zero não permitida")

print(f"{n1} * {n2} = {n1 * n2}")