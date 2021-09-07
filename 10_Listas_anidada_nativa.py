import random
SEPARADOR = ('*' * 20) + "\n"

#Creacion de una lista de cinco listas con diez elementos cada una
lista = [random.randrange(1,101) for valor in range(10)]
print(type(lista))
print(f"El primer elemento es {lista[0]} y el ultimo es {lista[9]}")
print(type(lista))
print(SEPARADOR)

#Creacion de una lista de cinco listas con diez elementos cada una
lista_de_listas = [[random.randrange(1,101) for valor in range(10)] for valor in range(5)]
print(lista_de_listas)
print(f"El primer elemento es {lista_de_listas[0][0]} y el ultimo es {lista_de_listas[4][9]}")
#print(lista_de_listas[0][:])
print(lista_de_listas[0])
for lista_interna in lista_de_listas:
    print(type(lista_de_listas))

print(type(lista_de_listas))

print("[")
for lista_primer_nivel in lista_de_listas:
    #print(f"Lista interna: {lista_primer_nivel}")
    print("[", end="")
    for elemento in lista_primer_nivel:
        print(f"{elemento}", end="\t")
    print("]", end="")
    print("")
print("]")
print(SEPARADOR)

print(f"El elemento 0,2 es {lista_de_listas[0][2]}")
print(f"El elemento 2,7 es {lista_de_listas[2][7]}")
#print(lista_de_listas[0,4]) #ESTO ES UN ERROR