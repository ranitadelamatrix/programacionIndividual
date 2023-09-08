from clases import *

print("**************************************")
print("*                                    *")
print("*        ¡Bienvenido a tu curso!     *")
print("*                                    *")
print("*                                    *")
print("**************************************")
print("")




usuario = int(input("Si usted desea registrase como estudiante presione 1\nSi usted desea registrarse como docente o administrador presione 2"))

if usuario == 1:
    print("Registrate como usuario para poder comprar y acceder al aula, a continuacion te pediremos unos datos")
    nombre = input('Nombre: ')
    apellido =input('Apellido: ')
    email=input('Email: ')
    celular = int(input("celular: "))
    dni = int(input("dni: "))
    nacimiento = input("fecha de nacimiento: ")
    direccion = input("dirección: ")
    localidad = input("localidad: ")
    codigo_postal = int(input("codigo postal: "))
    provincia = input("Provincia: ")

    usuario1 = RegistrarUsuario(nombre, apellido, dni, direccion, nacimiento, localidad, codigo_postal, provincia, celular, email)
    print(usuario1)
elif usuario == 2:
    usuario2 = Usuarios()
    usuario2.rol()