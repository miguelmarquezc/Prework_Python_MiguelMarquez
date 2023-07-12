"""
1. Ejercicio: Define una función que utilice un bucle para imprimir los primeros n números de la serie de Fibonacci.
"""


def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


fibonacci(10)

"""
2. Ejercicio: Define una función que tome un número y retorne una lista de sus divisores.
"""


def divisores(n):
    return [i for i in range(1, n + 1) if n % i == 0]


print(divisores(20))

"""
3. Ejercicio: Define una función que tome una lista y retorne una nueva lista con los elementos únicos de la lista original.
"""


def unicos(lista):
    return list(set(lista))


print(unicos([1, 2, 2, 3, 4, 4]))

"""
4. Ejercicio: Define una función que tome un número y retorne la suma de sus dígitos.
"""


def suma_digitos(n):
    return sum(int(digito) for digito in str(n))


print(suma_digitos(12345))

"""
5. Ejercicio: Define una función que tome una cadena y cuente el número de vocales en la cadena.
"""


def contar_vocales(cadena):
    return sum(1 for letra in cadena if letra.lower() in "aeiou")


print(contar_vocales("ThePower"))

"""
6. Ejercicio: Define una función que tome una lista y un número n, y retorne los primeros n elementos de la lista.
"""


def primeros_n_elementos(lista, n):
    return lista[:n]


print(primeros_n_elementos([1, 2, 3, 4, 5], 3))

"""
7. Ejercicio: Define una función que tome una cadena y retorne la cantidad de letras mayúsculas y minúsculas en la cadena.
"""


def contar_may_min(cadena):
    mayusculas = sum(1 for letra in cadena if letra.isupper())
    minusculas = sum(1 for letra in cadena if letra.islower())
    return mayusculas, minusculas


print(contar_may_min("ThePower"))

"""
8. Ejercicio: Define una función que tome un número y retorne True si es un número perfecto, False en caso contrario. Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos. Por ejemplo, 6 es un número perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3.
"""


def es_perfecto(num):
    return num == sum(divisor for divisor in range(1, num) if num % divisor == 0)


print(es_perfecto(6))

"""
9. Ejercicio: Define una función que reciba un número y retorne su representación en binario.
"""


def a_binario(n):
    return bin(n).replace("0b", "")


print(a_binario(15))

"""
10. Ejercicio: Define una función que reciba dos listas y retorne la intersección de ambas (los elementos que están en las dos listas).
"""


def interseccion(list1, list2):
    return list(set(list1) & set(list2))


print(interseccion([1, 2, 3, 4], [3, 4, 5, 6]))

"""
11. Ejercicio: Define una función que tome una cadena y determine si es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
"""


def es_palindromo(cadena):
    return cadena == cadena[::-1]


print(es_palindromo("ana"))

"""
12. Ejercicio: Escribe un programa que imprima los números del 1 al 50, pero para múltiplos de tres imprima “Fizz” en lugar del número y para los múltiplos de cinco imprima “Buzz”. Para números que son múltiplos de tanto tres como cinco imprima “FizzBuzz”.
"""
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

"""
13. Ejercicio: Define una función que tome una lista y retorne la lista ordenada en orden ascendente.
"""


def ordenar_lista(lista):
    return sorted(lista)


print(ordenar_lista([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))

"""
14. Ejercicio: Define una función que reciba una lista de palabras y un entero n, y retorne la lista de palabras que son más largas que n.
"""


def filtrar_palabras(lista_de_palabras, n):
    return [palabra for palabra in lista_de_palabras if len(palabra) > n]


print(filtrar_palabras(["The", "Power", "Data", "Analytics"], 5))

"""
15. Ejercicio: Define una función que tome un número y calcule su serie de Fibonacci.
"""


def serie_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib


print(serie_fibonacci(15))

"""
16. Ejercicio: Define una función que tome una lista de números y retorne el número más grande de la lista.
"""


def maximo(lista):
    return max(lista)


print(maximo([1, 10, 6, 15, 5]))

"""
17. Ejercicio: Define una función que reciba un número y retorne la suma de sus dígitos al cubo.
"""


def suma_cubos_digitos(n):
    return sum(int(digit) ** 3 for digit in str(n))


print(suma_cubos_digitos(123))

"""
18. Ejercicio: Define una función que reciba una lista de números y retorne el segundo número más grande de la lista.
"""


def segundo_maximo(lista):
    return sorted(set(lista), reverse=True)[1]


print(segundo_maximo([1, 3, 7, 7, 2, 5]))

"""
19. Ejercicio: Define una función que tome dos listas y retorne True si tienen al menos un miembro en común, de lo contrario, retorne False.
"""


def tienen_comun(lista1, lista2):
    return bool(set(lista1) & set(lista2))


print(tienen_comun([1, 2, 3], [3, 4, 5]))

"""
20. Ejercicio: Define una función que tome una lista y retorne una nueva lista con los elementos de la lista original en orden inverso.
"""


def invertir_lista(lista):
    return lista[::-1]


print(invertir_lista([1, 2, 3, 4, 5]))

"""
21. Ejercicio: Define una función que reciba una cadena y cuente el número de dígitos y letras que contiene.
"""


def contar_digitos_letras(cadena):
    digitos = sum(c.isdigit() for c in cadena)
    letras = sum(c.isalpha() for c in cadena)
    return digitos, letras


print(contar_digitos_letras("ThePower2023"))

"""
22. Ejercicio: Define una función que reciba una lista de números y retorne la suma acumulada de los números
"""


def suma_acumulada(lista):
    total = 0
    suma_acumulada = []
    for numero in lista:
        total += numero
        suma_acumulada.append(total)
    return suma_acumulada


print(suma_acumulada([1, 2, 3, 4, 5]))

"""
23. Ejercicio: Define una función que encuentre el elemento más común en una lista.
"""
from collections import Counter


def elemento_mas_comun(lista):
    return Counter(lista).most_common(1)[0][0]


print(elemento_mas_comun([1, 2, 3, 2, 4, 2, 5]))

"""
24. Ejercicio: Define una función que tome un número y retorne un diccionario con la tabla de multiplicar de ese número del 1 al 10.
"""


def tabla_de_multiplicar(numero):
    return {i: numero * i for i in range(1, 11)}


print(tabla_de_multiplicar(5))

"""
25. Ejercicio: Define una función que tome una cadena y retorne un diccionario con la cantidad de apariciones de cada caracter en la cadena.
"""


def contar_caracteres(cadena):
    return {caracter: cadena.count(caracter) for caracter in cadena}


print(contar_caracteres("hola hola"))

"""
26. Ejercicio: Define una función que tome dos listas y retorne la lista de elementos que no están en ambas listas.
"""


def elementos_no_comunes(lista1, lista2):
    return list(set(lista1) ^ set(lista2))


print(elementos_no_comunes([1, 2, 3, 4], [3, 4, 5, 6]))

"""
27. Ejercicio: Define una función que tome una lista y retorne la lista sin duplicados.
"""


def eliminar_duplicados(lista):
    return list(set(lista))


print(eliminar_duplicados([1, 2, 2, 3, 4, 4]))

"""
28. Ejercicio: Define una función que reciba un número entero positivo y retorne la suma de los cuadrados de todos los números pares menores o iguales a ese número.
"""


def suma_cuadrados_pares(n):
    return sum(i**2 for i in range(2, n + 1, 2))


print(suma_cuadrados_pares(6))

"""
29. Ejercicio: Define una función que reciba una lista de números y retorne el promedio de los números en la lista.
"""


def promedio(lista):
    return sum(lista) / len(lista)


print(promedio([1, 2, 3, 4, 5]))

"""
30. Ejercicio: Define una función que reciba una lista de cadenas y retorne la cadena más larga en la lista.
"""


def cadena_mas_larga(lista):
    return max(lista, key=len)


print(cadena_mas_larga(["The", "Power", "Data", "Analytycs"]))

"""
31. Ejercicio: Define una función que reciba un número entero n y retorne una lista con los n primeros números primos.
"""


def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
        return True


def primeros_n_primos(n):
    primos = []
    numero = 2
    while len(primos) < n:
        if es_primo(numero):
            primos.append(numero)
        numero += 1
    return primos


print(primeros_n_primos)

"""
32. Ejercicio: Define una función que reciba una cadena y retorne la misma cadena pero con las palabras en orden inverso.
"""


def invertir_palabras(cadena):
    return " ".join(cadena.split()[::-1])


print(invertir_palabras("The Power Data Analytics"))

"""
33. Ejercicio: Escribe una función que reciba una lista de tuplas y retorne una lista ordenada basada en el último elemento de cada tupla.
"""


def ordenar_por_ultimo_elemento(tuplas):
    return sorted(tuplas, key=lambda x: x[-1])


print(ordenar_por_ultimo_elemento([(1, 2), (3, 1), (4, 5)]))

"""
34. Ejercicio: Define una función que reciba una cadena y retorne la cantidad de letras vocales en la cadena.
"""


def contar_vocales(cadena):
    return sum(1 for c in cadena.lower() if c in "aeiou")


print(contar_vocales("The Power"))

"""
35. Ejercicio: Define una función que reciba un número entero y retorne True si es un número primo, de lo contrario retorne False."""


def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
        return True


print(es_primo(17))
