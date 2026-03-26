# lista de listas

ciclo = True

while ciclo:

    try:

        matriz = []

        n = int(input("Ingresa el tamaño de la lista: "))
        m = int(input("Ingresa el tamaño de la sublista: "))

        for i in range(n):

            fila = []

            for j in range(m):

                elemento = []

                elemento = input("Valor: ")

                fila.append(elemento)

            matriz.append(fila)

            print(matriz)

            ciclo = False

    except ValueError:
        print("Ingresa un dato válido")
        continue