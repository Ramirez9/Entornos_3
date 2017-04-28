#! -*- coding: UTF-8 -*-
'''
Escriba un programa que pida dos números enteros. El programa pedirá de nuevo el segundo número 
mientras no sea mayor que el primero. 
El programa terminará escribiendo los dos números.

@author: d16raruf
'''
print"EJERCICIO NÚMERO 2"
primero = int(input("Escriba un número: "))
segundo = int(input("Escriba un número mayor que " + str(primero) + ": "))

while segundo <= primero:
    print(segundo, "no es mayor que", str(primero) + ".Introduzca un numero nuevo: ")
    segundo = int(input())

print" "
print"Los numeros que ha escrito son", primero, "y", str(segundo) + "."
