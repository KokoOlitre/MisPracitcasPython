# La Funcion input sirve para capturar datos ingresados por el usuario desde la terminal Python, sin haberlos definido previamente.
# nombre = input( 'como te llamas?')

# print('Hola ' + nombre)

# edad = input('Cuantos años tienes?')
# print (type(edad))
# print (f'{nombre} tiene {edad} años') # f --> la frase formateada


# Programa que pide dos numeros al usuario y los suma

numero1 = int(input('Introduce un numero por favor:'))  # Int se pone para que lo ponga como entero de lo contrario lo toma como cadena
numero2 = int(input('Introduce otro numero por favor:')) # en cadena los concatena, 4 , 3 = 43, como entero los suma = 7
numero3 = numero1 + numero2

print(f'El resultado de la sunma es {numero3}')

