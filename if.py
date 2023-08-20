"""1. Pedirle al usuario que ingrese un número, si este es 10 se debe imprimir: ¡Usted ha
ganado el sorteo!
2. Sumar al ejercicio anterior, una pregunta: Si el número es menor imprimir: ¡Falto un poco,
seguí participando! Si es mayor, imprimir: ¡Te pasaste, a seguir intentando!"""



numero = int(input("hola bienvenidom, ingrese un numero por favor: "))

if numero == 10:
    print ("¡Usted ha ganado el sorteo!")
elif numero < 10:
    print ( "¡falto un poco, seguí participando")
else:
    print ('¡te pasaste,a seguirintentando!')

"""3. Pedirle al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro
mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día
ingresado no es ninguno de esos, imprimir otro mensaje."""

dia = input("hola amigo, ingresa un dia de la semana que te guste: ")

if dia.lower() == "lunes":
    print("elegiste ",dia, " arriba que comieza la semana.")
elif dia.lower() == "viernes":
    print("elegiste", dia," es porque se termina la semana perrys.")
elif dia.lower() == "sabado" or dia.lower() =="domingo":
    print("elegiste ",dia , " como te gusta no trabajar e")
else:
    print('para este dia ', dia , "no tengo una frase alentadora 'sorry'")

"""4. Escribir un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje
“es vocal”."""

letra = input("hola bienvenido, ingrese una letra por favor. ")
if letra in ["a","e","i","u"]: #aqui decimos que cree una lista y que si tiene estas letras imprima el msj
    print("la letra seleccionada es una vocal")
else:
    print("seleccionaste un tipo de letra que no es vocal perdiste un premio")

"""1. Escribir un programa que realice la sumatoria de los números que se quiera hasta ingresar
hasta que se ingrese -1.

2. Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a
introducir). El programa debe informar de cuantos números introducidos son mayores que
0, menores que 0 e iguales a 0.

3. Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso
contrario, el programa termina cuando se introduce un cero.
4. Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la
media de todos los números introducidos."""