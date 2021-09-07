'''
Ejemplo para demostrar el manejo de listas
Demuestra: Creacion,  acceso a elementos, ordenamiento y comprension de listas
'''
SEPARADOR = ("*" * 20) + "\n"

#Creacion de listas
#Lista vacia
lista_vacia = list()
otra_lista_vacia = []
#Lista con elementos iniciales
lista_uno = [1, 2, 3, 4]
print(lista_uno)
print(SEPARADOR)
pass #pass es en realidad una declaracion null que se usa generalmente como marcador
#de posicion. Cuando quiera declarar una funcion o un bucle pero no quiera proporcionar la implementacion,
# entonces puedo usar la sentencia pass

#Agregar elementos a listas existentes
lista_uno.append(5)
print(lista_uno)
lista_uno.append((6, 7)) #Una lista puede ser un elemento de otra lista
print(lista_uno)
print(SEPARADOR)
pass



#Remover elementos de una lista
lista_uno.remove((6, 7)) #Se le pasa el valor del elemento a remover
print(lista_uno)
print(SEPARADOR)
pass


#Ordenar elementos de una lista
#sort()
lista_original1 = [3, 4, 2]
print(lista_original1)
lista_original1.sort()
print(lista_original1)
pass



#sorted()
lista_original2 = [23, 10, 30, 5]
lista_ordenada = sorted(lista_original2)
print(f"Lista original = {lista_original2}, y la version ordenada es {lista_ordenada}")
print(SEPARADOR)
pass




#Comprension de listas
print(f"Lista original = {lista_uno}")

#SIN compresion de listas
lista_uno_al_doble = []
for valor in lista_uno:
    lista_uno_al_doble.append(valor * 2)
print(f"Lista resultante, cada elemento al doble = {lista_uno_al_doble}")
pass

#CON comprension de listas
lista_uno_al_doble = [valor * 2 for valor in lista_uno]
print(f"Mismo resultado, pero con comprension de listas = {lista_uno_al_doble}")
pass

#Comprension de listas con condicion
lista_valores_pares = [valor for valor in lista_uno if (valor % 2 ==0)]
print(f"Solamente se agregaron los elementos con valor par: {lista_valores_pares}")