from random import randint

from sys import path
path.append("modules")

from module import suml as suma, prodl as producto, __counter as contador

lista = [randint(-5,5) for i in range(15)]
print(lista)
print(suma(lista))
print(producto(lista))
print(contador)