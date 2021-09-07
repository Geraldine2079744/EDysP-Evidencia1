'''
Demostracion de implementacion de pilas utilizando listas y con deques
'''
import collections
SEPARADOR =("*" * 20) + "\n"

pila_con_lista = list()
for i in range(5):
    pila_con_lista.append(input("Dime el nombre a agregar: "))

#Sacar elementos de la pila
while pila_con_lista:
    print(pila_con_lista.pop())
print(SEPARADOR)

#Una cola doblemente terminada, o deque, admite agregar y eliminar elementos
# de cualquier extremo de la cola.
#Las pilas y colas mas comunes son formas degeneradas de deques,
# donde las entradas y salidas estan restringidas a un solo extremo.

pila_deque = collections.deque()
for i in range(5):
    pila_deque.append(input("Dime el nombre a agregar: "))

#Sacar elementos de la pila
while pila_deque:
    print(pila_deque.pop())
pass