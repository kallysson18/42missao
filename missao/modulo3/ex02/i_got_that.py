#!/usr/bin/env python3
"""Use um loop while que aceite continuamente a entrada do usuário e responda
com "Eu entendi! Mais alguma coisa?"após cada entrada.
O loop deve parar apenas quando o usuário inserir "STOP".
"""
word = input("What you gotta say?: ")
while word != "STOP":
    word = input("i got that! Anything else? :")
 
