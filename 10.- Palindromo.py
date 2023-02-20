"""Definir una función es_palindromo() 
que reconoce palíndromos (es decir, palabras que tienen 
el mismo aspecto escritas invertidas), 
ejemplo: es_palindromo ("radar") tendría que devolver True.
"""

palabra = "radar" #Se alamacena en la variable palabra la palabra que será evaluada.

def es_palindromo(pal): #Se crea la función "es_palindromo"
    invert = pal[::-1] #Se almacena en la variable invert la palabra invertida.
    if pal == invert: #Evalúa si la palabra inversa y original son iguales.
        return True #Si la palabra es palíndromo retorna True.
    else: #En otro caso que la palabra inversa no sea igual a la original.
        return False #Retorna False de no ser palíndromo.
    
print(es_palindromo(palabra)) #Llama a la función e imprime lo que retorne la misma.