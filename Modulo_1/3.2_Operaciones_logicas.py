
"""
Realiza un programa que solicite al usuario que introduzca tres números
luego realiza las siguientes verificaciones lógicas.

Paso 1: Solicitar tres números al usuario.
    Nota: Usa la función input() para pedir al usuario que introduzca tres números.
        La función float() se usa para convertir el valor introducido en un número decimal.
Paso 2: Verificar si los tres números son positivos.
Paso 3: Verificar si al menos uno de los números es negativo.
Paso 4: Verificar si el primer número es mayor que el segundo y el segundo es mayor que el tercero.
Paso 5: Mostrar los resultados.
    Nota: Usa la función print() para mostrar los resultados.
"""

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))


# ------------------------------------------------------------------
# En está sección agregar su codigo

todos_positivos =  num3 > 0 and num2 > 0 and num1 > 0

al_menos_un_negativo = num3 or num2 or num1 <0

orden = num1
# -------------------------------------------------------------------





print(f"Los tres números son positivos: {todos_positivos}")
print(f"Al menos uno de los números es negativo: {al_menos_un_negativo}")
print(f"El primero es mayor que el segundo y el segundo es mayor que el tercero: {orden}")