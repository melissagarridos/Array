# ==============================
# CRUD CON DICCIONARIOS, LISTAS Y TUPLAS
# ==============================

# Diccionario principal (inventario)
inventario = {}

# Lista de categorías
categorias = ["Tecnología", "Hogar", "Ropa"]

# ==============================
# CREATE (Crear producto)
# ==============================
def crear_producto():
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    
    print("Categorías disponibles:", categorias)
    categoria = input("Seleccione categoría: ")

    # Tupla (dato fijo: código y categoría)
    datos_fijos = (len(inventario) + 1, categoria)

    inventario[nombre] = {
        "precio": precio,
        "cantidad": cantidad,
        "datos": datos_fijos
    }

    print("✅ Producto agregado\n")


# ==============================
# READ (Mostrar inventario)
# ==============================
def mostrar_productos():
    if not inventario:
        print("Inventario vacío\n")
        return
    
    for nombre, info in inventario.items():
        codigo, categoria = info["datos"]
        
        print(f"""
Producto: {nombre}
Código: {codigo}
Categoría: {categoria}
Precio: {info['precio']}
Cantidad: {info['cantidad']}
        """)


# ==============================
# UPDATE (Actualizar producto)
# ==============================
def actualizar_producto():
    nombre = input("Producto a actualizar: ")

    if nombre in inventario:
        nuevo_precio = float(input("Nuevo precio: "))
        nueva_cantidad = int(input("Nueva cantidad: "))

        inventario[nombre]["precio"] = nuevo_precio
        inventario[nombre]["cantidad"] = nueva_cantidad

        print("🔄 Producto actualizado\n")
    else:
        print("❌ Producto no encontrado\n")


# ==============================
# DELETE (Eliminar producto)
# ==============================
def eliminar_producto():
    nombre = input("Producto a eliminar: ")

    if nombre in inventario:
        del inventario[nombre]
        print("🗑 Producto eliminado\n")
    else:
        print("❌ Producto no encontrado\n")


# ==============================
# CRUD adicional en LISTAS
# ==============================
def gestionar_categorias():
    print("1. Agregar categoría")
    print("2. Eliminar categoría")
    opcion = input("Opción: ")

    if opcion == "1":
        nueva = input("Nueva categoría: ")
        categorias.append(nueva)
        print("✅ Categoría agregada\n")

    elif opcion == "2":
        eliminar = input("Categoría a eliminar: ")
        if eliminar in categorias:
            categorias.remove(eliminar)
            print("🗑 Categoría eliminada\n")
        else:
            print("❌ No existe\n")


# ==============================
# MENÚ PRINCIPAL
# ==============================
def menu():
    while True:
        print("""
1. Crear producto
2. Mostrar productos
3. Actualizar producto
4. Eliminar producto
5. Gestionar categorías (listas)
6. Salir
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
            gestionar_categorias()
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción inválida\n")


# Ejecutar programa
menu()
