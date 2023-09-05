import re 

from validate_email_address import validate_email


"""Por cada curso se deberá visualizar la fecha de comienzo, título, descripción, objetivos,
programa, costo, duración en meses, foto y estado (disponible o no disponible, en base a su
estado deberán verse o no en el sitio) <---datos, atributos). 

A su vez, cada curso pertenece a alguna de las
siguientes categorías (Inicial, Intermedio, Avanzado)<---metodos."""



class Curos1():
    #de esta forma creamos los atributos de inicializacion
       
       def __init__(self, fecha, titulo, descripcion, objetivos, programa, costo, foto, duracion_meses, estado, categoria) -> None:
                self.fecha = fecha
                self.titulo = titulo
                self.descripcion = descripcion
                self.objetivos = objetivos
                self.programa = programa
                self.costo = costo
                self.foto = foto
                self.duracion_meses = duracion_meses
                self.estado = estado
                self.categoria = categoria
                self.listadeclases = []

       def __str__(self) -> str:
          return f"Hola bienvenido al curso el mismo comieza el dia {self.fecha}\nnuestro curso se llama {self.titulo}\nen el veremos {self.descripcion}\nnuestro objetivo es que {self.objetivos}\nnuestro programa es {self.programa}\nel curso tiene un valor de {self.costo}\ntu foto de perfil es {self.foto}\nel mismo tiene una duracion de {self.duracion_meses} meses\nel curso se encuentra {self.estado}"
    
       def estado_del_curso(self): #metodo disponibilidad
                if self.estado == "disponible":
                        print("el curso  esta disponible")
                else:
                        print("el curso no esta disponible")
       def categoriaCurso(self):
               if self.categoria == 1:
                      return ("inicial")
               elif self.categoria == 2:
                      return ("intermedio")
               else:
                      return ("avanzado")
      
       def verclases(self):
              for i in self.listadeclases:
                     print(f" fecha {i[0]}, el titulo {i[1]}, contenido {i[2]}, la direccion del drive {i[3]}")
        
"""Por otro lado, los cursos contienen un conjunto de clases,
en donde por cada clase se debe
mostrar la fecha, título, contenido, URLDrive."""
curiiii = Curos1("22.55.88", "uno", "probando", "aprender", "2", 4000, "foto.png", 8, "disponible", "inicial")

class Clases():
        
       def __init__(self, fecha, titulo, contenido, URLDrive):
              self.fecha = fecha
              self.titulo = titulo
              self.contenido = contenido
              self.URLDrive = URLDrive
          
       

v = Clases("23.85.99", "cmica", "matriz", "wwwww")





"""Cada clase de un curso la dicta un docente, y este puede participar en el dictado de varias
clases y de varios cursos. De cada docente se desea guardar su apellido, nombre, dni, fecha
nacimiento, dirección, localidad, código postal, provincia, teléfono celular, email."""

class Docente():
       def __init__(self, apellido, nombre, dni, nacimiento, direccion, localidad, codigo_postal, provincia, celular, email):
              self.apellido = apellido
              self.nombre = nombre
              self.dni = dni
              self.nacimiento = nacimiento
              self.direccion = direccion
              self.localidad = localidad
              self.codigo_postal = codigo_postal
              self.provincia = provincia
              self.celular = celular
              self.email =email

       def __str__(self) -> str:
              return f"DATOS DEL DOCENTE\nApellido {self.apellido}\nNombre {self.nombre}\nDNI {self.dni}\nNacimiento {self.nacimiento}\nDireccion {self.direccion}\nLocalidad {self.localidad}\nCodigo Postal {self.codigo_postal}\nProvincia {self.provincia}\ntelefono celular {self.celular}\nEmail {self.email}"
       
docent = Docente("terjo", "gaston", 33669317, "02/06/1988", "catamarca 2660", "villa maria", 5900, "cordoba", 385417268, "gastontrejo9099@hotmail.com")


"""Por otra parte, los interesados en inscribirse a un curso deberán crearse una cuenta de usuario
final, donde deberán registrar su datos personales (nombre, apellido, dni, dirección, fecha
nacimiento, dirección, localidad, código postal, provincia, teléfono celular, email) además de
confirmar y reconfirmar una clave de acceso. Para la activación de la cuenta de usuario final se
deberá validar que el email sea verdadero y esté en funcionamiento, enviando un correo
automático al email registrado."""

class RegistrarUsuario():
       
       def __init__(self, nombre, apellido, dni, direccion, nacimiento, localidad, codigo_postal, provincia, celular, email):
              self.apellido = apellido
              self.nombre = nombre
              self.dni = dni
              self.nacimiento = nacimiento
              self.direccion = direccion
              self.localidad = localidad
              self.codigo_postal = codigo_postal
              self.provincia = provincia
              self.celular = celular
              self.email = email

       def validacion(self):
                            
                     if validate_email(self.email) == True and not re.match(r"[^@]+@[^@]+\.[^@]+", self.email) == False:
                            
                            print("su direccion valido")
                            print("---------->CORRABORE SUS DATOS<-----------")
                            print(" Nombre:",self.nombre,"\n","Apellido:",self.apellido ,"\n","DNI:", self.dni,"\n","Fecha de nacimiento: ", self.nacimiento,"\n","Direccion: ",self.direccion ,"\n", "Localidad:",self.localidad,"\n","Codigo Postal:",self.codigo_postal,"\n","Provincia:",self.provincia,"\n","Celualr:",self.celular,"\n","Email:",self.email)
                            correcion = int(input("Si sus datos son correcto presione 1, si no lo son presione cualquier tecla "))

              

                            if correcion == 1:
                                   generar = input("Genere su contraseña, recuerde que ambas deben coincidir, presione enter para continuar")
                                   while True:
                                          clave1 = input("Ingrese una clave por favor: ")
                                          clave2=input ("Repita la clave para confirmarla: ")
                                          if clave1==clave2:
                                                 print(f"Se a enviado un correo automatico a {self.email} para su validacion")
                                                 break
                                          else:
                                                 print("no coinciden las contraseñas vuelva a intentar ")
                            else:
                                   print("corrabore sus datos")
                     else:
                            print("correo no valido")
              
              



a = RegistrarUsuario("gaston", "trejo", 336699, "vatamar", "12/15/15", "villa maria", 5900, "cordoba", 3854172687, "gastontrejo9099@hotmail.com")




"""Los usuarios públicos registrados pueden inscribirse a uno o más cursos. Además, el sitio
deberá proveer la posibilidad de registrar 2 roles más de usuarios quienes también tendrán
interacción con el sistema: Administrador, Docente. Los usuarios también deben tener
asociado un estado (Activo / Inactivo)."""

class Usuarios():
       def __init__(self, usuarios, cursos)->None:
              self.usuarios = usuarios
              self.cursos = cursos
       def inscripcionCurso(self):
              self.listaCursos = []
              if self.usuarios.validacion() == True:
                     self.listaCursos.append(self.cursos)
                     print("se agrego un curso")
              else:
                     print("no se aegrego")

abb = Usuarios(a, curiiii)
abb.inscripcionCurso()

"""Por último, los usuarios finales podrán agregar uno o más cursos en un carrito de compras,
donde se deberá visualizar: Foto, título del curso, duración, costo. Una vez confirmados los
ítems del carrito, deberá seleccionar el medio de pago, los cuales pueden ser: Tarjeta de
crédito/débito y transferencia bancaria; a fin de tener más datos acerca de los medios de
pago, deberán registrarse los datos básicos de tarjetas y transferencias). Al confirmar la
compra, se deberá registrar además la fecha de compra, el usuario que realiza la compra y el
monto total. Dada la consigna anterior, se pide: identificar, analizar y documentar los
requisitos según el formato de historias de usuario. Para la creación de las historias, hacer uso
del repositorio Github, a través de creación de issues."""