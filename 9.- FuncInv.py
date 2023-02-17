"""Definir una función inversa() 
que calcule la inversión de una cadena. 
Por ejemplo la cadena "estoy probando" 
debería devolver la cadena "odnaborp yotse"""

string = "estoy probando" #Se crea la variable de cadena de texto.

def inversa(str): #Se define la función inversa para revertir las cadenas de texto.
    cont = -1 #Se crea la variable cont que funciona como contador para comenzar desde el último elemento de la cadena de texto.
    reverseString = "" #Variable para almacenar la cadena de texto revertida.
    for i in str: #Bucle para ejecutar la cuenta regresiva de la cadena.
        reverseString += str[cont] #Almacena el caracter desde el final al principio.
        cont -= 1 #Resta uno para que la cuenta aumente y se pueda usar valores a la derecha.

    print(reverseString) #Imprime la cadena de texto inversa.

inversa(string) #Se llama a la función creada pasando el parámetro de cadena de texto.