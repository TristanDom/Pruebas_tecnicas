"""Definir una función max_de_tres(), 
que tome tres números como argumentos y 
devuelva el mayor de ellos."""

def max_de_tres(val1, val2, val3): #Se declara el la función del mayor de los tres números
    if val1 > val2 and val1 > val3: #Se declara la condicional if la cual evaluará si el primer valor es el mayor.
        print("El primer valor es el mayor: ", val1) #Se imprime que el primer valor es el mayor.
    elif val2 > val1 and val2 > val3: #La condicional elif evalúa si el segundo valor es el mayor.
        print("El segundo valor es el mayor: ", val2) #Imprime que el segundo valor es el mayor.
    elif val3 > val1 and val3 > val2: #Evalúa si el tercer es el siguiente.
        print("El tercer valor es el mayor: ", val3) #Imprime que el valor tercer valor es el mayor.
    else: #En caso que ninguo sea mayor que otro los tres son del mismo tamaño por lo tanto son iguales.
        print("Los tres números son iguales: ", val1) #Imprime que los tres valores son iguales.

while True:
    num1 = input("Digita el primer valor: ") #Se realiza input del primer valor.
    num2 = input("Digita el segundo valor: ") #Se realiza input del segundo valor.
    num3 = input("Digita el tercer valor: ") #Se realiza input del tercer valor.
    max_de_tres(num1, num2, num3) #Llama a la función retornando un resultado.
