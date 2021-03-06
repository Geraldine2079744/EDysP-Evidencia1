'''
Implementacion de colas mediante deque()
Demuestra las diferencias en la forma de implementacion
'''

SEPARADOR = ("*" * 20) + "\n"
import collections

cola = collections.deque()   #Cola utilizzando deque

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
    print(cola.popleft())
pass   #Verificar que la estructura se encuentra vacia