"""En la variable text dispones de una cadena de texto.
Debe contar las palabras y devolver cuantas veces se repiten cada una de ellas.
"""
# Texto a transformar.
text = "Creo que a veces es la gente de la que nadie espera nada, la que hace cosas que nadie puede imaginar"

# Función para convertir el texto a minúsculas.
# Se ocupa la función lower() para convertir el texto a minúsculas y se retorna el resultado.
def convText2lower(a):
    a = text.lower()
    return a

# Función para quitar las marcas del texto.
# Se ocupa la función replace() para quitar las marcas como la coma y el punto, retornando el resultado.
def quitMarks(b):
    tnm = b.replace(',', '').replace('.', '')
    return(tnm)

# Función para convertir el texto en una lista.
# Se ocupa la función split() para convertir el texto en una lista, retornando el resultado.
def conv2list(c):
    convTxt = c.split(" ")
    return(convTxt)

# Función para contar las palabras que se repiten.
# Se ocupa un diccionario para contar las palabras que se repiten, retornando el resultado con un bucle para contar si una palabra ya se ha agregado al diccionario, de lo contrario se cuanta que aún no.
def contRepWords(d):
    # Se crea un diccionario vacío el cual va a contener las palabras y el número de veces que se repiten.
    dic = {}

    # Se crea un bucle para contar las palabras que se repiten.
    for word in d:        
        # Si la palabra ya se encuentra en el diccionario, se suma 1 al valor de la palabra.
        if word in dic:
            dic[word] += 1
        # De lo contrario se agrega la palabra al diccionario con un valor de 1.
        else:
            dic[word] = 1
    return dic

# Se llama a las funciones para realizar la conversión del texto.
textoConv = convText2lower(text)
textoConv = quitMarks(text)
textoConv = conv2list(text)
textoF = contRepWords(textoConv)

# Imprime el texto que se va a transformar y el resultado de la transformación.
# Este código se puedealterar de tal forma que solo se muestren las palabras que se repitieron cierto número de veces.
print("El texto es: ", text)
print(textoF)