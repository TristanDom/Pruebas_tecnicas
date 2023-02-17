"""Escribir una función sum() y 
una función multip() que sumen y multipliquen respectivamente 
todos los números de una lista. Por ejemplo: sum([1,2,3,4]) 
debería devolver 10 y multip([1,2,3,4]) debería devolver 24."""

lista = [1, 2, 3] # Lista que se solicita para el llenado de información en las funciones.

def sum(list): #Se define la función de suma.
    suma = 0 #Se crea la variable suma inicializada con cero para almacenar la suma de los valores.
    for i in list:  #Se crea bucle for para la iteración de la lista y poder sumar cada valor de la misma.
        suma += i #Se almacena la suma de las iteraciones en la varible creada con anterioridad.
    print(suma) #Imprime la suma total del bucle.

def mult(list): #Se define la función de multiplicación.
    multi = 0 #Se crea la variable multi inicializada con cero para almacenar la multiplicación de los valores.
    for e in list: #Se crea bucle for para la iteración de la lista y poder multiplicar cada valor de misma.
        multi += e #Se almacena la multiplicación de las iteraciones en la variable creada con anterioridad.
    print(multi) #Impime la multiplicación total el bucle.
    
sum(lista) #Se hace el llado a al función sum con el parámetro lista que es la lista de los valores.
mult(lista) #Se hace el llado a al función mult con el parámetro lista que es la lista de los valores.