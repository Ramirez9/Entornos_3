#! -*- coding: UTF-8 -*-
'''
Escriba un programa que pida la anchura y altura de un rectángulo y 
lo dibuje con caracteres producto (*):

@author: Francisco Ramírez Ruiz
'''
print"EJERCICIO NÚMERO 4"

altura = int(input("Altura del rectángulo: "))
anchura = int(input("Anchura del rectángulo: "))

for i in range(altura):
    print "*",
    for j in range(anchura-1):
        print "*",
    print " "
    