#! -*- coding: UTF-8 -*-
'''
Escriba un programa que permita crear una lista de palabras (que puede ser vacía). 
Para ello, el programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista. 
Por último, el programa tiene que escribir la lista.

@author: Francisco Ramírez
'''
print"EJERCICIO NÚMERO 5"

numero = int(input("Introduzca la cantidad de palabas que tiene la lista: "))

if numero < 1:
    print("La lista no puede estar vacía!")
else:
    lista = []
    for i in range(0,numero):
        palabra= raw_input("Digame la palabra: ")
        lista.append(palabra)
    print("La lista creada es:", lista)
