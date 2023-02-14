"""
Se da una cadena de texto y se pide que:
Se extraigan los dígitos del mismo.
Ordene de menor a mayor y los devuelva en una cadena de texto.
Sume los dígitos obtenidos y devuelva los resultados en una suma total.
Estos resultados deverán ser mostrados de manera sumultanea.
"""
# El método que he usado para la resolución de este problema es usando el menor número de funcione del sistema posible, se podría simplificar considerablemente con el uso de funciones del sistema.


# Se proporciona una cadena de carcteres en la cual se tendrá que extraer los dígitos.
text = "fjh2jekfj980f123we9uvjh2430978fwhaskj2jhcuyh2"
# Lista vacía para almacenar los dígitos.
list = []
listOrd = []
listInt = []

# Se inicializa una lista de dígitos para ser comparados con los de la cadena de texto.
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

StringDig = ""
sumDig = 0

for i in text:
    if i in digits:
        list.append(i)

for j in digits:
    for k in list:
        if k == j:
            listOrd.append(k)

for m in listOrd:
    StringDig += m

for n in listOrd:
    listInt.append(int(n))

for p in listInt:
    sumDig += p

print("Números obtenidos: ")
print(list)

print("Números ordenados en lista: ")
print(listOrd)

print("Números ordenados en entero: ")
print(listInt)

print("Númeos ordenados y mostrados en una cadena de texto: ")
print(StringDig)

print("Súma de números: ")
print(sumDig)