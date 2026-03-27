import json


datos = {
    1:{
    "nombre": "Luisa",
    "edad": 22,
    "ciudad": "Quilla",
    "habilidades": ["Python", "JSON"]
},
2:{
    "nombre": "Jander",
    "edad": 23,
    "ciudad": "Barranquilla",
    "habilidades": ["Python", "Java"]
}}

with open('datos.json', 'w', encoding='utf-8') as f:
    json.dump(datos, f, indent=4)
print("Archivo JSON creado exitosamente.")



with open('datos.json', 'r', encoding='utf-8') as f:
    datos_leidos = json.load(f)

print(datos_leidos)


print(f"Nombre: {datos_leidos["2"].get('nombre')}")

print("La edad de luisa es: ",datos_leidos["1"].get("edad"))


with open('datos.json', 'r', encoding='utf-8') as f:
    datos_actuales = json.load(f)

datos_actuales["3"] = {
    "nombre": "Hillary",
    "edad": 19,
    "ciudad": "Medellin",
    "habilidades": ["JavaScript", "HTML"]
}

with open('datos.json', 'w', encoding='utf-8') as f:
    json.dump(datos_actuales, f, indent=4, ensure_ascii=False)

print("Nueva persona agregada correctamente.")

with open('datos.json', 'r', encoding='utf-8') as f:
    datos_leidos = json.load(f)

print(datos_leidos)
