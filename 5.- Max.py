"""Definir una función max() que tome como argumento dos números y 
devuelva el mayor de ellos. (Es cierto que python tiene una función max() 
incorporada, pero hacerla nosotros mismos es un muy buen ejercicio."""

num1 = input("Digita el primer valor: ")
num2 = input("Digita el segundo valor: ")

def max(val1, val2):
    if val1 > val2:
        print("El número más grande es: ", val1)
    elif val2 > val1:
        print("El número más grande es: ", val2)
    else:
        print("Ambos valores son iguales.")

max(num1, num2)