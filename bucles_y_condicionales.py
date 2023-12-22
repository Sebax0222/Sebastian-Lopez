
bucles

ejercicio 1 ------------------------


numero = int(input("Ingrese un número:"))
print(f"Tabla de multiplicar de {numero}:")
for i in range(1, 11):
    resultado = numero * i
    
    print(f"{numero} x {i} = {resultado} " )

#Ejercicio 2 ---------------------------------

numero = int(input("Ingrese un número entero: "))

suma_enteros = 0

for x in range(2, numero + 1, 2):
    suma_enteros += x
    

print(f"La suma de los números pares desde 2 hasta {numero} es: {suma_enteros}")

#Ejercicio 3 -----------------------------------

lineas = 5

for x in range (lineas + 1):
    print('*' * x)



#--------------------------------------------------------------------------------------------------------------------------------

condicionales y bucles

#Ejercicio 1---------------------


num = int(input("ingrese numero"))
suma_pares = 0
for x in range(1, num + 1):
    if x % 2 == 0: 
        suma_pares += x
        print(f" suma de numeros pares desde 1 hasta {num} es: {suma_pares}")


#Ejercicio 2 ----------------------

palabra = input("Ingrese una palabra: ")

contador_vocales = 0

palabra = palabra.lower()

indice = 0

while indice < len(palabra):
    caracter = palabra[indice]
    if caracter in "aeiou":
        contador_vocales += 1
    indice += 1

print(f"La cantidad de vocales en la palabra es: {contador_vocales}")


#Ejercicio 3 -------------------

numero = int(input("Ingrese un número entero positivo mayor que 1: "))

#Es_primo = True

for i in range(2, int(numero**0.5) + 1):
    if numero % i == 0:
        es_primo = False
        break


if es_primo:
    print(f"{numero} es un número primo.")
#Else:
    print(f"{numero} no es un número primo.")

#Ejercicio 4 ------------------------------------------------------------------------------------------------

import random

numero_secreto = random.randint(1, 100)

print("¡Bienvenido al juego de adivinanzas!")
print("Intenta adivinar el número secreto entre 1 y 100.")

intentos = 0

while True:
    intento = int(input("Ingresa tu intento: "))
    
    intentos += 1

    if intento == numero_secreto:
        print(f"¡Felicidades! ¡Adivinaste el número secreto {numero_secreto} en {intentos} intentos!")
        break
    elif intento < numero_secreto:
        print("Demasiado bajo. Intenta de nuevo.")
    else:
        print("Demasiado alto. Intenta de nuevo.")

#Ejercicio 5 -------------------------------------------------------------------------------------------

numero = int(input("Ingrese un número: "))


if numero % 2 == 0:
    for i in range(numero):
        print('*', end=' ')
else:
    for i in range(numero):
        print('* ' * numero)