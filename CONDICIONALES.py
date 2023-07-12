'''
1. Ejercicio: Dado un número, imprime si es positivo o negativo.
2. Ejercicio: Dado un número, imprime si es par o impar.
3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos.
'''

#Ejercicio 1
numero = 10
if numero > 0:   
    print("Positivo")
else:    
    print("Negativo")

#Ejercicio 2

numero = 6
if numero % 2 == 0:
    print("Par")
else:   
    print("Impar")

#Ejercicio 3

a, b, c = 5, 7, 2
mayor = max(a, b, c)
print(mayor)
