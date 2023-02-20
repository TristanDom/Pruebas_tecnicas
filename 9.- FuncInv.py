"""Definir una función inversa() 
que calcule la inversión de una cadena. 
Por ejemplo la cadena "estoy probando" 
debería devolver la cadena "odnaborp yotse"""

string = "estoy probando" #Se crea la variable de cadena de texto.

def inversa(str): #Se define la función inversa para revertir las cadenas de texto.
    cadena_inversa = str[::-1] #Almacena en la variable cadena inversa el inverso de la cadena.
    return cadena_inversa #Retorna la palabra inversa.

print(inversa(string)) #Se llama a la función creada pasando el parámetro de cadena de texto.