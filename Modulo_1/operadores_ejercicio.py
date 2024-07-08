"""
Escribir un programa que solite dos numeros y luego imprima:
1. suma de dos numeros
2. resta del primer numero menos el segundo
3.el producto de los dos numeos
4.El cubo de la suma de los dos numeros
5 el cociente de la division del primer numero por el segundo
"""
#es del tipo floar para ingresar un numero
number_one = float(input("Ingrese el primer numero:"))
number_two = float(input("Ingrese el segundo numero"))
#imprimimos las operaciones
print({number_one + number_two}) #1
print({number_one - number_two})#2
print({number_one * number_two})#3
print({(number_one + number_two)**3})#4
print({number_one / number_two})