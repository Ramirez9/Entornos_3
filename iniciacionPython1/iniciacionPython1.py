#! -*- coding: UTF-8 -*-
'''
Escriba un programa que pida dos números enteros y 
que calcule su división, escribiendo si la división es exacta o no.

@author: Francisco Ramírez Ruiz
'''

print"EJERCICIO NÚMERO 1"
dividendo = int(input("Escriba el dividendo: "))
divisor = int(input("Escriba el divisor: "))

cociente = dividendo // divisor
resto = dividendo % divisor

if dividendo % divisor == 0:
    print("La división es exacta.")
else:
    print("La división no es exacta.")