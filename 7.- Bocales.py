"""Escribir una función que tome un caracter y 
devuelva True si es una vocal, de lo contrario devuelve False."""

def vocal(valor): #Se declara la función para detectar si el caracter es vocal o no.
    vocales = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'] #Lista de vocales para tomar como referencia en la comparación.
    if valor in vocales: #Declaración de la condicional if para la evalución del caracter.
        print(True) #Si la condicional encontró al caracter dentro de la lista imprime True.
    else: #Sentencia condicional en otro caso.
        print(False) #Imprime False

val = input("Digite un caracter para ser evaluado: ") #Input para almacenar en variable el caracter.
vocal(val) #Se llama a la variable vocal.