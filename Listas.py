# Listas empizan con corchetes []
peliculas = ["Lion King", "The Beauty and the Beast", "Mulan", "Mulan"]
print("Toda la lista: ", peliculas)
print("Toda la lista: ", peliculas[0])
# it is exclusive, will just include position 0 and 1
print("Toda la lista: ", peliculas[0:2]) 
print("Toda la lista: ", peliculas[1:]) 
# agregar elementos a la lista
peliculas.append("movie4")
print("Toda la lista: ", peliculas)
peliculas2 = ["Coco", "Cinderella", "Mulan"]
# concatenar la lista peliculas 2 a peliculas
peliculas.extend(peliculas2)
print("Toda la lista: ", peliculas)
# insertar una nuevan pelicula en una posicion especifica
peliculas.insert(1, "La Sirenita")
print("Toda la lista: ", peliculas)
# saber la posicion de una pelicula dada
print("Mulan se encuentra en la posicion ", peliculas.index("Mulan")+1)
# saber si se repite un elemento en la lista
print("Mulan se repite", peliculas.count("Mulan"), "veces") # no hay necesidad de agregar espacios antes y despues de las frases, lo hace solo
# saber si un elemento esta en la lista
print("Blanca Nieves esta en la lista?", "Blanca Nieves" in peliculas)
print("Mulan esta en la lista?", "Mulan" in peliculas)
# Eliminar elementos de una lista basado en nombre, si hay varias con el mismo nombre borra la primera
peliculas.remove("movie4")
print("Nueva list ", peliculas)
# Eliminar elementos de una lista basado en index
ultimaPeli = peliculas.pop()
print(ultimaPeli)
print("New List", peliculas)
# cambiar el orden de la lista
peliculas.reverse()
print("Lista en reversa", peliculas)
# ordernar lista, no importa el tipo de dato
peliculas.sort()
print("Lista Ordenana", peliculas)


# HW 1
# 1. Imprimir la lista de atras hacia adelante
print("HW1 Q1 - Start")
print("Lista impresa de atraz hacia adelante")
# refect to length of the list
for i in range(len(peliculas)):
    print(peliculas[len(peliculas)-1-i])
print("HW1 Q1 - End")    

# 2. Usar al lista peliculas y eleminar los repetidos
print("HW1 Q2 - Start")
print("Lista con repetidos:", peliculas)
newlist = list(set(peliculas))
print("Lista sin repetidos:", newlist)
print("HW1 Q2 - End")

# trabajar con operadorees
peliculas2 = ["Coco", "Cinderella", "Mulan"]
# print 3 times the same list
print(peliculas2*3)
# imprimir 2 o mas listas juntas sin necesidas de concanetenar una a la otra
peliculas3 = ["The steepy beauty", "Mickey Mouse"]
print(peliculas2+peliculas3)
# si el 3 esta en la lista [1, 2, 3] sin necesidad de crear la lsita primero
print(3 in [1, 2, 3])
print(2 in [1, 2, 3])


# HW 2
# 1. Read documentation of the method set in python.