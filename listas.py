# ==============================
# CRUD CON LISTAS
# ==============================

# Lista principal
productos = []

# ==============================
# CREATE (Agregar producto)
# ==============================
def crear_producto():
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    productos.append(producto)
    print("✅ Producto agregado\n")


# ==============================
# READ (Mostrar productos)
# ==============================
def mostrar_productos():
    if not productos:
        print("Lista vacía\n")
        return

    for i, p in enumerate(productos):
        print(f"""
ID: {i}
Nombre: {p['nombre']}
Precio: {p['precio']}
Cantidad: {p['cantidad']}
        """)


# ==============================
# UPDATE (Actualizar producto)
# ==============================
def actualizar_producto():
    mostrar_productos()
    try:
        index = int(input("ID del producto a actualizar: "))

        if 0 <= index < len(productos):
            nuevo_precio = float(input("Nuevo precio: "))
            nueva_cantidad = int(input("Nueva cantidad: "))

            productos[index]["precio"] = nuevo_precio
            productos[index]["cantidad"] = nueva_cantidad

            print("🔄 Producto actualizado\n")
        else:
            print("❌ ID inválido\n")

    except ValueError:
        print("❌ Error en los datos\n")


# ==============================
# DELETE (Eliminar producto)
# ==============================
def eliminar_producto():
    mostrar_productos()
    try:
        index = int(input("ID del producto a eliminar: "))

        if 0 <= index < len(productos):
            productos.pop(index)
            print("🗑 Producto eliminado\n")
        else:
            print("❌ ID inválido\n")

    except ValueError:
        print("❌ Error en los datos\n")


# ==============================
# MENÚ
# ==============================
def menu():
    while True:
        print("""
1. Crear producto
2. Mostrar productos
3. Actualizar producto
4. Eliminar producto
5. Salir
        """)

        opcion = input("Seleccione: ")

        if opcion == "1":
            crear_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida\n")


# Ejecutar
menu()
