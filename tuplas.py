# Tuplas

tupla = ("melissa", 23, "junior", "mia", "brandy","mia")

print(tupla)

mia = tupla.count("mia")

brandy = tupla.index("brandy")


print(f"cantidad de mias: {mia} y posición de brandy: {brandy}")


# nombre,edad,perro1,perro2,perro3,perro4 = tupla

i,*j,k = tupla

# i agarra el primero

# *j agarra lo demas

# k agarra el ultimo


print(*j)

nombre, edad, nivel, perro1, perro2, repetido = tupla

print(nombre)   # melissa

print(perro1)   # mia

print(perro2)   # brandy


