
'''
Ejemplo para ilustrar la importacion de la libreria random en Python 3
Demuestra el uso de: randrange(stop),randrange(start,stop,step), random(),choice(seq),shuffle(seq)
'''
import random
SEPARADOR = ("*" * 20) + "\n"

print(f"Obteniendo un numero entero aleatorio que puede ir del 0 al 30: {random.randrange(30)}")
print(SEPARADOR)
print(f"Obteniendo un numero entero aleatorio para que pueda ir del 2 al 30: {random.randrange(2, 31, 2)}")
print(SEPARADOR)
print(f"Obteniendo un valor numerico entre 0.0 y 1.0: {random.random()}")
print(SEPARADOR * 2)

listaDePrueba = [10, 30, 15, 45]
print(f"La lista de prueba es {listaDePrueba}")
print(f"El valor seleccionado aleatoriamente de la lista anterior es {random.choice(listaDePrueba)}")
print(SEPARADOR)
random.shuffle(listaDePrueba)
"La funcion random, shuffle devuelve la secuencia x pasada como argumento desordenada."
print(f"La lista ya 'perturbada/barajada' es {listaDePrueba}")