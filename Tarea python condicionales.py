#Ejercicio número 1
numero = int(input('ingrese un número: '))

if (numero % 2) == 0:
    print('par')
else:
    print('impar')


# #-------------------------------------------------
# #Ejercicio número 2


    edad = int(input("Ingrese su edad: "))

    if edad < 18:
        print("Eres menor de edad")
    elif edad >= 18 and edad <= 65:
        print('Eres un adulto')
    else:
        print('Eres un adulto mayor')
    
    
# #-----------------------------------------------
# #Ejercicio número 3

    edad = int(input('ingrese su edad'))
    precio = float(input('ingrese el precio del producto'))

    if edad < 18: 
        print('El costo de su producto es ' + str(precio * .90))
    elif edad >= 65:
        print('El costo de su producto es' + str(precio * .85))
    else:
        print('El costo de su producto es ' + str(precio))

# #-------------------------------------------------------
# #Ejercicio número 4

    puntuacion = int(input('Ingrese su puntuación'))

    if puntuacion >= 90:
        print('Sobresaliente')
    elif puntuacion >= 80 and puntuacion <= 89:
        print('Bueno')
    elif puntuacion >= 70 and puntuacion <= 79:
        print('Satisfactorio')
    elif puntuacion >= 60 and puntuacion <= 69:
        print('Necesita mejorar')
    else:
        print('Reprobado')

# #--------------------------------------------------------
# #Ejercicio número 5

    salario = float(input('Ingrese su salario para calcular el impuesto'))

    if salario < 10000:
        print('No aplica un impuesto')
    elif salario > 10000 and salario <= 50000:
        print('Debe pagar el 10% de impuesto, para un valor de '+ str(salario * .1))
    elif salario > 50000 and salario <= 100000:
        print('Debe pagar el 20% de impuesto, para un valor de '+ str(salario * .2))
    else:
        print('Debe pagar el 30% de impuesto, para un valor de '+ str(salario * .3))





