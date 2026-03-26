
coders = {

    1 : {
        
        "id": 1001918240,
        "nombre": "melissa",
        "apellido": "garrido",
        "ingles": "c1"
    },
    2 : {
        "id": 1009831992,
        "nombre": "luisa",
        "apellido": "de la rosa",
        "ingles": "b1"
    },
    3 : {
        "id": 1001983829,
        "nombre": "diego",
        "apellido": "fontalvo",
        "ingles": "b2"
    }
}

sw = True

while sw:

    print("""Listado de coders
          1. Buscar coder
          2. Agregar coder
          3. Eliminar coder
          4. Ver listado
          5. Salir\n""")
    

    opcion = input("\nDigite la opción: ").strip()

    try:

        opcion = int(opcion)

        if opcion == 1:

            print("\nBuscando el nombre de un coder especifico")

            n = input("\nEscriba el nombre del coder: ").strip().lower()

            coder_encontrado = None

            for llave, datos in coders.items():
                
                if datos.get("nombre") == n:

                    coder_encontrado = datos
                    break

            if coder_encontrado:
                    
                print(coder_encontrado)
                    
            else:

                print("Not found")
                
            volver = input("\nSi desea volver al menú digite (SI): ").lower().strip()

            if volver == "si":
                sw = True
            else:
                sw = False


        elif opcion == 2:

            print(coders)

            try:

                nombre = input("\nNombre: ").strip().lower()

                apellido = input("\nApellido: ").strip().lower()

                ingles = input("\nIngles: ").strip().lower()

                id = int(input("\nID: ")).strip()

                #Nuevo coder

                coders[4] = {"id":id,"nombre":nombre, "apellido":apellido, "ingles": ingles}

                print("\nImprimiendo luego de añadir otro coder")

                print(coders)

            except ValueError:

                print("Ingrese datos válidos")

            volver = input("\nSi desea volver al menú digite (SI): ").lower().strip()

            if volver == "si":
                sw = True
            else:
                sw = False


        elif opcion == 3:

            print(coders)

            n = input("\nDigite número de coder a eliminar: ")

            try:

                n = int(n)

                print(coders.get(n,"\nNo encontrado"))

                if n in coders:

                    del coders[n]

                    print(coders)

            except ValueError:

                print("\nValue error")

            volver = input("\nSi desea volver al menú digite (SI): ").lower().strip()

            if volver == "si":
                sw = True
            else:
                sw = False


        elif opcion == 4:

            print(coders)

            volver = input("\nSi desea volver al menú digite (SI): ").lower().strip()

            if volver == "si":
                sw = True
            else:
                sw = False


        elif opcion == 5:

            print("\nSaliendo...")
            sw = False


    except ValueError:
        print("\nDigite una entrada válida")

        volver = input("\nSi desea volver al menú digite (SI): ").lower().strip()

        if volver == "si":
            sw = True
        else:
            sw = False

       