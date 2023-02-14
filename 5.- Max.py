"""Definir una función max() que tome como argumento dos números y 
devuelva el mayor de ellos. (Es cierto que python tiene una función max() 
incorporada, pero hacerla nosotros mismos es un muy buen ejercicio."""

num1 = input("Digita el primer valor: ") #Input del primer valor.
num2 = input("Digita el segundo valor: ") #Imput del segundo valor.

def max(val1, val2): #Función que eligirá el mayor número de dos que se proporcione.
    if val1 > val2: #Se declara la condicional que eligirá el valor más grande.
        print("El número más grande es: ", val1) #Imprime si el primer valor es más grande.
    elif val2 > val1: #Evalúa si el segundo valor es más grande que el primero.
        print("El número más grande es: ", val2) #Imprime si el segundo valor es más grande.
    else: #En caso que ninguno de los dos valores sea más grande uno que otro.
        print("Ambos valores son iguales.") #Imprime enunciado que ninguno de los dos valores es más grande que otro.

max(num1, num2) #Se llama a la función y se le pasan los valores para que esta sea ejecutada correctamente.