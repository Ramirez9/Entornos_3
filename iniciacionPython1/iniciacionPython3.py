#! -*- coding: UTF-8 -*-
'''
Escriba un programa que pida un entero mayor que cero y a continuación 
pida esa cantidad de números positivos.

@author: Francisco Ramírez Ruiz
'''

print"EJERCICIO NÚMERO 3"
objetivo = int(input("Introduzca los números que desea: "))
while objetivo < 1:
    objetivo = int(input("La cantidad tiene que ser mayor que 0. Intentelo de nuevo: "))

print" "
numero = int(input("Escriba un número: "))
cantidad = 1

while cantidad < objetivo:
    cantidad += 1
    segundo = int(input("Escriba otro número más: "))

print" "
if cantidad == 1:
    print"Ha escrito 1 número positivo."
else:
    print"Ha escrito", cantidad, "numeros positivos."

