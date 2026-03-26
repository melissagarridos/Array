coders = {
    1: {
        "id": 1048229292,
        "nombre": "Jander",
        "apellido": "Arguello",
        "edad": 30,
        "nvlIngles": "-A0"
    },
    2: {
        "id": 1048229296,
        "nombre": "Luisa",
        "apellido": "De la Rosa",
        "edad": 19,
        "nvlIngles": "C30"
    },
    3: {
        "id": 1048229297,
        "nombre": "Maria",
        "apellido": "Sanchez",
        "edad": 19,
        "nvlIngles": "C1"
    }
}


print(coders)

nombre = input("dig un nombre: ")

#Nuevo coder

coders[4] = {"id":100203033,"nombre":nombre, "apellido":"Guzman","edad": 20, "nvlIngles": "B2"}

print("imprimiendo luego de añadir otro coder\n")

print(coders)

print("Buscando el nombre de un coder especifico")

print(coders[4]["nombre"])

print("Buscando con el metodo get")

print(coders.get(1, "No encontrado"))



print("Buscando por numero de documento")

busqueda_id = 1048229298
coder_encontrado = None

for llave, datos in coders.items():
    if datos["id"] == busqueda_id:
        coder_encontrado = datos

print(coder_encontrado)