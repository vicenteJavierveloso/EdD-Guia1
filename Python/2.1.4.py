#crear_identidad: list -> list
#Funcion que dada una matriz cuadrada de orden n
#Entrega una matriz identidad de orden n
#Ej:matriz = [[1,2,3,4],[3,2,1,3],[3,1,2,3],[3,2,1,5]]
#   crear_identidad(a) -> [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
def crear_identidad(a:list):
    filas = len(a)
    columnas = len(a[0])
    if filas == columnas:
        identidad = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                if i == j:
                    fila.append(1)
                else:
                    fila.append(0)
            identidad.append(fila)
        return identidad
    else:
        return None

#aumentar_matriz: list list -> list
#Funcion que aumenta una matriz A con una matriz B de la misma cantidad de filas entregando (A|b)
#Ej: matriz = [[1,2,3,4],[3,2,1,3],[3,1,2,3],[3,2,1,5]]
#    matriz_identidad = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
def aumentar_matriz(a:list,b:list):
    if len(a)==len(b):
        for i in range(len(a)):
            a[i] += b[i]
        return a
    else:
        return None

# def escalarxfila(escalar:int,fila:int,matriz:list):
#     fila = matriz[fila]
#     for i in range(len(fila)):
#         fila[i] = fila[i]*escalar
#     return fila

# def sumarfilas(fila1:list,fila2:list):
#     for i in range(len(fila1)):
#         fila1[i] = fila1[i]+fila2[i]
#     return fila1

matriz = [[1,2,3,4],[3,2,1,3],[3,1,2,3],[3,2,1,5]]

matriz_identidad = crear_identidad(matriz)
#Aumentar
matriz_aumentada = aumentar_matriz(matriz,matriz_identidad)
print(matriz_aumentada)