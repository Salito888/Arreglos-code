# Taller Arreglos Primer Corte- Salomè Granada Henao

# Ejercicio 1
# Se inicializa un arreglo vacìo
numeros = []

for i in range(10):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

# Mayor número y posición
mayor_num = numeros[0]
pos_mayor = 0

for i in range(1, len(numeros)):
    if numeros[i] > mayor_num:
        mayor_num = numeros[i]
        pos_mayor = i
# Salida
print(f"El mayor número es {mayor_num} y está en la posición {pos_mayor}.")

# Ejercicio 2
def es_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Inicializar arreglo vacìo
arreglo = []
print("Ingresa 10 números enteros:")
for i in range(10):
    numero = int(input(f"Número {i + 1}: "))
    arreglo.append(numero)

# Nùmero primo mayor y posiciòn
may_primo = None
posicion_mayor_primo = -1

for i, num in enumerate(arreglo):
    if es_primo(num):
        if may_primo is None or num > may_primo:
            may_primo = num
            posicion_mayor_primo = i

# Salida
if may_primo is not None:
    print(f"El mayor número primo es {may_primo} y está en la posición {posicion_mayor_primo}.")
else:
    print("No se encontraron números primos en el arreglo.")

# Ejercicio 3
def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Crear una lista para almacenar los números primos
primos = []

# Encontrar números primos entre 100 y 300
for num in range(100, 301):
    if es_primo(num):
        primos.append(num)
        if len(primos) == 10:  # Si ya tenemos 10 números primos, detener la búsqueda
            break

# Mostrar los números primos en pantalla
print("Números primos entre 100 y 300:")
for primo in primos:
    print(primo)

# Ejercicio 4
# Paso 1: Leer 10 números enteros del usuario
numeros = []
for i in range(10):
    num = int(input(f"Introduce el número entero {i+1}: "))
    numeros.append(num)

# Paso 2: Determinar las posiciones de los números que terminan en 4
posiciones = []
for i, num in enumerate(numeros):
    if num % 10 == 4:
        posiciones.append(i)

# Paso 3: Imprimir las posiciones encontradas
print("Las posiciones de los números que terminan en 4 son:")
for pos in posiciones:
    print(pos)

# Ejercicio 5
# Inicializar arreglo de nùmeros vacìo
numeros = []
for i in range(10):
    num = int(input(f"Introduce el número entero {i+1}: "))
    numeros.append(num)

# Mayor nùmero del arreglo
mayor = max(numeros)

# Contar las veces que se repite el nùmero mayor
contador = numeros.count(mayor)

# Salida
print(f"El mayor número es {mayor} y aparece {contador} veces.")

# Ejercicio 6
# Inicializar un arreglo vacìo
numeros = []
print("Introduce 10 números enteros:")

for i in range(10):
    num = int(input(f"Número {i + 1}: "))
    numeros.append(num)

# Promedio Entero
suma = sum(numeros)
promedio = suma // len(numeros)  # División entera

# Verificar si se encuentra el promedio en el arreglo
if promedio in numeros:
    print(f"El promedio entero ({promedio}) está en el arreglo.")
else:
    print(f"El promedio entero ({promedio}) no está en el arreglo.")

# Ejercicio 7

def suma_digitos(n):
    """Devuelve la suma de los dígitos del número entero n."""
    return sum(int(digit) for digit in str(abs(n)))

# Inicializar un arreglo vacìo
numeros = []
print("Introduce 10 números enteros:")

for i in range(10):
    num = int(input(f"Número {i + 1}: "))
    numeros.append(num)

# Nùmero- suma de dìgitos
max_suma_digitos = -1
posicion_max = -1

for i in range(len(numeros)):
    suma_actual = suma_digitos(numeros[i])
    if suma_actual > max_suma_digitos:
        max_suma_digitos = suma_actual
        posicion_max = i

# Salida
print(f"El número con la mayor suma de dígitos es {numeros[posicion_max]} en la posición {posicion_max}.")

# Ejercicio 8

import math

# Inicializar con un arreglo vacìo para ingresar los nùmeros
numeros = []
for i in range(10):
    numero = int(input(f"Ingresa el número entero {i + 1}: "))
    numeros.append(numero)

# Factorial de los nùmeros
factores = [math.factorial(num) for num in numeros]

# Se muestra cada nùmero con su respectivo factorial
for num, fac in zip(numeros, factores):
    print(f"El factorial de {num} es {fac}")

# Ejercicio 9
# Arreglo vacìo para ingresar los nùmeros
numeros = []
print("Introduce 10 números enteros:")

for _ in range(10):
    while True:
        try:
            num = int(input("Número: "))
            numeros.append(num)
            break
        except ValueError:
            print("Por favor, introduce un número entero válido.")

# Mostrar los enteros comprendidos entre 1 y cada número del arreglo
for numero in numeros:
    print(f"Enteros comprendidos entre 1 y {numero}:")
    for i in range(1, numero + 1):
        print(i, end=' ')
    print()  # Nueva línea para separar las salidas

# Ejercicio 10

# Definir el número de estudiantes
MAX_ESTUDIANTES = 50

# Inicializar arreglos para almacenar los datos de los estudiantes
cedulas = []
sexos = []
sueldos = []
trabaja = []

# Leer la cantidad de estudiantes
N = int(input("Ingrese el número de estudiantes (N <= 50): "))

# Verificar que el número de estudiantes sea válido
if N > MAX_ESTUDIANTES or N <= 0:
    print("Número de estudiantes no válido.")
else:
    # Leer los datos de los estudiantes
    for i in range(N):
        print(f"\nEstudiante {i + 1}:")
        cedula = input("Cédula: ")
        sexo = int(input("Sexo (1: masculino, 2: femenino): "))
        sueldo = int(input("Sueldo: "))
        trabaja_estudiante = int(input("Trabaja (1: sí, 2: no): "))

        # Almacenar los datos en los arreglos
        cedulas.append(cedula)
        sexos.append(sexo)
        sueldos.append(sueldo)
        trabaja.append(trabaja_estudiante)

    #  Porcentajes y Promedios
    total_hombres = sexos.count(1)
    total_mujeres = sexos.count(2)

    if total_hombres > 0:
        total_trabajan_hombres = sum(1 for i in range(N) if sexos[i] == 1 and trabaja[i] == 1)
        total_sueldo_hombres_trabajan = sum(sueldos[i] for i in range(N) if sexos[i] == 1 and trabaja[i] == 1)
        porcentaje_hombres_trabajan = (total_trabajan_hombres / total_hombres) * 100
        promedio_sueldo_hombres_trabajan = (
                    total_sueldo_hombres_trabajan / total_trabajan_hombres) if total_trabajan_hombres > 0 else 0
    else:
        porcentaje_hombres_trabajan = 0
        promedio_sueldo_hombres_trabajan = 0

    if total_mujeres > 0:
        total_trabajan_mujeres = sum(1 for i in range(N) if sexos[i] == 2 and trabaja[i] == 1)
        total_sueldo_mujeres_trabajan = sum(sueldos[i] for i in range(N) if sexos[i] == 2 and trabaja[i] == 1)
        porcentaje_mujeres_trabajan = (total_trabajan_mujeres / total_mujeres) * 100
        promedio_sueldo_mujeres_trabajan = (
                    total_sueldo_mujeres_trabajan / total_trabajan_mujeres) if total_trabajan_mujeres > 0 else 0
    else:
        porcentaje_mujeres_trabajan = 0
        promedio_sueldo_mujeres_trabajan = 0

    porcentaje_hombres = (total_hombres / N) * 100
    porcentaje_mujeres = (total_mujeres / N) * 100

    # Salida
    print(f"\nPorcentaje de hombres en la universidad: {porcentaje_hombres:.2f}%")
    print(f"Porcentaje de mujeres en la universidad: {porcentaje_mujeres:.2f}%")
    print(f"Porcentaje de hombres que trabajan: {porcentaje_hombres_trabajan:.2f}%")
    print(f"Sueldo promedio de los hombres que trabajan: {promedio_sueldo_hombres_trabajan:.2f}")
    print(f"Porcentaje de mujeres que trabajan: {porcentaje_mujeres_trabajan:.2f}%")
    print(f"Sueldo promedio de las mujeres que trabajan: {promedio_sueldo_mujeres_trabajan:.2f}")
