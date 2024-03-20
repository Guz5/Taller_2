# Comentario de una linea
# Todo lo que va después es ignorado por el 
# interprete en Python

# Variables: Espacio de memoria, con nombre, donde guardo valores
# Los nombres de variables deben der cortos, descriptivos, NO TENER ESPACIOS
# EN BLANCO ni caracteres especiales, no deben empezar por un número

# Descriptivo signifíca que representa la ategoría del dato que quiero guardar
# En python las variables pueden contener cualquier dato de tipo primitivo
# numeros (enteros, reales), cadenas de carácteres (string), booleanos (True, False)
# carateres (letras).

variable = 1

variables = "un informante de los bajos fondos me puso una cita en un bar de mala muerte del centro de la ciudad"

variables = True

variables = 'a'

variables = 3.1415926535

#Para asignar un valor a la varible se usa el operador =

#Operadores: mecanismo par obtener un dato a partir de otros datos.
# Los datos que intervienen se llaman operandos.

#Aritméticos: + - / %
#De comparación: retornan True o False. < > <= >= == !=
#Los de lógica booleana: AN OR, Retornan True o False de a cuerdo a una
#tabla de verdad. Los operadores booleanos y de comparacion son muy utilizados al
#definir condiciones

a = True
b = False
print(a and b)

#Los operadores booleanos y de coomparacion son muy utilizados al 
#definir condiciones


#Sentencias de control de flujo: En general un programa se ejecuta
#linea por línea de manera secuencial. Se puede romper esa secuencialidad
#empleando un conjunto de sentencias (expreciones) que permite:
# 1. Seleccionar la ejecución de un bloque de código
# 2. Repetir la ejecución de un blque de código
# 3. Seleccionar entre ejecuta un bloque de codigo u otro bloque de código
# De esa manera podemos "romper" la seuencialidad
# Principios del paradigma de programacion estructurado

#Sentencia if. Si se cumple una condicion (se valua como True)
#se ejecuta un bloque de código

print("---------Otro código---------") 

print("Línea 1")
print("Línea 2")

print("---------Otro código---------") 

if 5>8 or 3<1:
    print("Esto se muestra si la condicion es verdadera")
else:
    print("Esto se muestra si la condición es falsa")
    
print("---------Otro código---------") 
    
entrada=int(input("¿cuantos años tiene?:"))

if entrada<18:
    print("usted está chiquito")
else: 
    print("Ya está grande, deje de llorar")