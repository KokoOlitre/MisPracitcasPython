# Operadores aritmeticos
# print (2 + 2) # suma
# print (4 - 2) # Resta
# print (3 * 7) # Multiplicacion
# print (15 / 2)
# print (11 % 4) # Modulo. 11 modulo 4 ( se ve solo el residuo de una divicion)
# print (11 // 4) # Divicion de piso. doble diagonal para refernencia de doble operador de piso (en divicion el resultado de la divicion,cuanto cabe de manera entera el 4 en el 11)
# print (2 ** 3 )  # Potenciacion. doble asterisco es para elevar a la potencia

# Operadores en cadenas
# print('Hola ' + 'mundo') # no se llama suma . Concatenacion
# print ('hola' * 3) # No es multiplicacion. Repeticion
# print('Hola ' + 'mundo'  * 3)

#Operadores de Comparacion. Permiten verificar si un elemento es igual a otro. o si un elemento es mayor que otro.
# print ('Hola' =='hola')  # == representa igual que
# print ('Hola' !='hola')  # == representa distinto que
# print (3 > 11 )  # < representa menor que  3 mayor que 11, resultado False
# print (11 >= 10 )  # >= representa mayor o igual que
# print (10 <= 10 )  # >= representa menor o igual

# Operadores de existencia. Verifica si un elemento existe dentro otro elemento
# print('ola' in 'Hola') # Verifica si la cadena 'ola' esta en la cadena 'Hola' --> True
# print('ola' not in 'Hola') # Verifica si la cadena 'ola' no se encuentra en la cadena 'Hola' --> False


# Operadores Booleanos. Verifican si se cumple una u otra condicion.
# Print (True or False) # Or verifica que se cumpla solo una de las condiciones
# Print (True and False) # AND verifica se cumplan las dos condiciones

#Operadores de asignacion
# x = 1 # operador de asignacion estandar
# x += 2 # Operador de asignacion suma
# x *= 3 # Operador de asignacion multiplicacion
# x %= 4 # Operador de asignacion Modulo
# print (x)

# los operadores se resulven primero los parentesis, exponentes, multiplicaciones, diviciones, modulos, doble piso, sumas y restas.
# Si hay operadores del mismo nivel se resuelven de Izquierda a aderecha

x =  6 * 5 + 8 / 2 ** 4
print (x)