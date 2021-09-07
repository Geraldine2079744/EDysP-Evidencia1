'''
Ejemplo para ilustrar la importancia de la libreria "sys" y "os" en Python 3
Demuestra el uso de: sys.getsizeof(x), os.getcwd(), os.walk()
'''
import sys
import os
SEPARADOR = ("*" * 20) + "\n"

#Uso del modulo sys
lista = list()
for numero in range(1, 1001):
    lista.append(numero)

print(f"La lista tiene {len(lista)} elementos y tiene un tamaño de {sys.getsizeof(lista)} bytes")
print(SEPARADOR)

tupla = tuple(lista)
print(f"La tupla tiene {len(tupla)} elementos y tiene un tamaño de {sys.getsizeof(tupla)} bytes")
print(SEPARADOR)

#Uso del modulo os
print(f"El directorio actual de trabajo es {os.getcwd()}")

for raiz, dirs, archivos in os.walk(".", topdown=False): #Demostracion de unpacking
    for nombre in archivos:
        print(os.path.join(raiz, nombre))
    for nombre in dirs:
        print(os.path.join(raiz, nombre))