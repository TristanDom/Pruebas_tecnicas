"""
Crear una función que devuelva una lista ordenada de menor a mayor
No se puede usar la funión sorted() ni librerías
"""

# Para solucionar la problemática se usa el método de ordenamiento burbuja.

list = [7, 5, 4, 9, 2]

def ord_burbuja(arreglo):
    n = len(arreglo)

    for i in range(n-1):       # <-- bucle padre
        for j in range(n-1-i): # <-- bucle hijo
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]

ord_burbuja(list)

print(list)
    