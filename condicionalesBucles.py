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

dia = input("hola amigo, ingresa un dia de la semana que te guste: ").lower()

if dia == "lunes":
    print("elegiste ",dia, " arriba que comieza la semana.")
elif dia == "viernes":
    print("elegiste", dia," es porque se termina la semana perrys.")
elif dia == "sabado" or dia =="domingo":
    print("elegiste ",dia , " como te gusta no trabajar e")
else:
    print('para este dia ', dia , "no tengo una frase alentadora 'sorry'")

"""4. Escribir un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje
“es vocal”."""

letra = input("hola bienvenido, ingrese una letra por favor. ")
if letra in ["a","e","i","u"]: #aqui decimos que cree una lista y que si tiene estas letras imprima el msj
    print(f"es vocal la letra {letra}")
else:
    print("seleccionaste un tipo de letra que no es vocal perdiste un premio")

"""1. Escribir un programa que realice la sumatoria de los números que se quiera hasta ingresar
hasta que se ingrese -1."""

suma = 0
while True:
    numero = int(input("ingrese numero que desa sumar, o ingrese -1 para terminar: "))
    if numero !=-1 :
        suma = suma + numero
        
    else:
        
        print(f"la sumatoria de los numeros es: {suma}",)
        print("finalizo la suma, gracias")
        
        break
        

"""2. Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a
introducir). El programa debe informar de cuantos números introducidos son mayores que
0, menores que 0 e iguales a 0."""
print("=== Bienvenido al programa. ===")
numeros = int(input("ingrese la cantidad de numeros que desea ingresar por favor: "))
mayor_0 = 0
menor_0 = 0
igual_0 = 0


for nu in range(numeros):
    valor_numero=float(input(f"ingresa 1 numeros a la vez: "))
    mayor_0+= valor_numero > 0
    menor_0+= valor_numero < 0
    igual_0+= (valor_numero==0 )
print(f"la cantidad de numeros ingresados son {numeros}, de los cuales estos son los resultados")
print(f"mayores a 0: {mayor_0}, menores a 0: {menor_0}, iguales a 0: {igual_0}")

"""3. Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso
contrario, el programa termina cuando se introduce un cero."""

print("bienvenido, ingresa un caracter para corraborar, ingresa 0 para terminar")
while True:
    
    caracter = input("Ingresa el caractere por favor: ").lower()
    if caracter == "0":
        print("FIN DEL PROGRAMA")
        break
    if len(caracter) >= 1:
        if caracter in {"a","e","i","o","u"}:
            print(f"VOCAL")
            print("")
        else:
            print("NO VOCAL")
            print("")
    else:
        print("NO INGRESO UN CARACTER")
        print("")

    
"""4. Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la
media de todos los números introducidos."""

sumaTotal = 0
cantidadIngresada = 0

print("=== Bienvenido al programa, ingrese un numero, para terminar ingrese 0. ===")
while True:
    numerito = float(input("ingrese un numero por favor: "))
    if numerito != 0:
        sumaTotal += numerito
        cantidadIngresada +=1
        media = sumaTotal / cantidadIngresada
        
    else:
        print(f"La suma total de los numeros ingresados es {sumaTotal} y la media es {media}")
        break