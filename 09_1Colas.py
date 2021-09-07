'''
Implementacion de colas mediante listas y deque()
Demuestra las diferencias en la forma de implementacion
'''

#Las colas(Tuplas) Son colecciones de elementos ordenados que unicamente permiten dos acciones:
#Añadir un elemento a la cola. Sacar un elemento de la cola.

SEPARADOR = ("*" * 20) + "\n"

cola = list()  #Cola utilizando una lista

for cantidad in range(5):
    nuevo = input("Nombre del recien llegado: ")
    cola.append(nuevo)

print(f"Se agregaron {len(cola)}, elementos: ")
for elemento in cola:
    print(elemento)
print(SEPARADOR)
pass  #Hacer notar que los elementos permanecen en la cola

print("Procedemos a retirarlos de la cola")
while cola:
    print(cola.pop( ))
pass  #Verificar que la estructura se encuentre vacia
#El metodo pop() elimina y retorna un elemento de una lista. Hay un parametro opcional, el indice al ser eliminado de la lista,
#si no se especifica ningun indice, a. pop() elimina y retorna el ultimo elemento de la lista