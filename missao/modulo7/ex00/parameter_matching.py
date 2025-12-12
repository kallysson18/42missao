#!/usr/bin/env python3

import sys 
# pega os parametros passados na linha de comando (incluindo o nome do arquivo) 
parametros = sys.argv
# Verifica se o número de parâmetros (excluindo o nome do script) é 1
if len(parametros) != 2:
    print("none")
    exit()
# O parâmetro que eu quero comparar   
palavra_certa = parametros[1]

entrada_usuario = input("What was the parameter?")

if palavra_certa == entrada_usuario:
    print("Good Job!")
else:
    print("Nope, sorry...")

