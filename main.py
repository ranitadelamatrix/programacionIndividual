from clases import *

print("**************************************")
print("*                                    *")
print("*        ¡Bienvenido a tu curso!     *")
print("*                                    *")
print("*                                    *")
print("**************************************")
print("")





def registracionn():
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
        usuario1.validacion()

    elif usuario == 2:
        usuario2 = Usuarios()
        usuario2.rol()

def verLosCursos():
    print("Estos son los cursos disponbles")
    print(matematicas.titulo, lengua.titulo, informatica.titulo)
    ver = int(input("si desea ver el contenido presione 1"))
    if ver == 1:
        print("Estos son los cursos disponbles")
        print(matematicas)
        print("")
        input("siguiente curso, presione enter para continuar")
        print(lengua)
        print("")
        input("siguiente curso, presione enter para continuar")
        print(informatica)
        print("")
    else:
        print("gracias")


def comprar():
    matematicas = Curos1("22/09/2023", "matematicas", "polinomios", "aprender las funciones", "numero 1", 6000, "foto.jpg", 6, "disponible", "avanzado")
    lengua = Curos1("22/09/2023", "lengua", "verbo", "aprender las ingles", "numero 1", 9000, "foto.jpg", 6, "no disponible", "inicial")
    informatica = Curos1("22/09/2023", "informatica", "base de datos", "aprender crud", "numero 1", 12000, "foto.jpg", 6, "disponible", "avanzado")
    mate = Carrito(matematicas)
    info = Carrito(informatica)
    comprar = int(input(f"si desea comprar los cursos presione1\nSi no presione 2"))
    
    if comprar == 1:
        pagar = Pagos()
        pagar.mediosPagos("gaston")




