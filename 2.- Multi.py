# Haz una función multiplicar que no utilice el símolo de multiplicación.
"""
Puesto que la base de la multiplicación es la suma se puede aplicar para que una función
pueda ejecutarse se puede aplicar la misma base para la función.
"""
# Forma número uno.
# Función para multiplicar dos números de forma recursiva.
def multiplicar(a, b):
    # Se crea un bucle para sumar el multiplicando por el número de veces por el multiplicador.
    for i in range(b - 1):
        # Cada que se repita el bucle se suma el multiplicando al resultado.
        a += b
    # Retorna el resultado.
    return a

# Forma número dos.
# Función para multiplicar dos números de forma recursiva.
def multiplicar1(a, b):

    result = 0
    # Se crea un bucle para sumar el multiplicando por el número de veces por el multiplicador.
    for i in range(b):
        # Cada que se repita el bucle se suma el multiplicando al resultado.
        result += a
    # Retorna el resultado.
    return result

# Se llama la primera función.
print(multiplicar(8, 8))

# Se llama la segunda función.
print(multiplicar1(50, 50))