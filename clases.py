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
        

        def __str__(self) -> str:
          return f"Hola bienvenido al curso el mismo comieza el dia {self.fecha}\nnuestro curso se llama {self.titulo}\nen el veremos {self.descripcion}\nnuestro objetivo es que {self.objetivos}\nnuestro programa es {self.programa}\nel curso tiene un valor de {self.costo}\ntu foto de perfil es {self.foto}\nel mismo tiene una duracion de {self.duracion_meses} meses\nel curso se encuentra {self.estado}"
    
        def estado_del_curso(self): #metodo disponibilidad
                if self.estado != "disponible":
                        print("el curso no esta disponible")
                else:
                        print("el curso esta disponible")
        def categoriaCurso(self):
               if self.categoria == 1:
                      return ("inicial")
               elif self.categoria == 2:
                      return ("intermedio")
               else:
                      return ("avanzado")
        def clsesvarias(self):
               self.clase = []

        def ingresarClases(self, fecha, titulo, contenido, URLDrive):
               
               nuevaclase = Clases(fecha, titulo, contenido, URLDrive)
               self.clase.append(nuevaclase)
        


               
"""Por otro lado, los cursos contienen un conjunto de clases<--metodos ,
en donde por cada clase se debe
mostrar la fecha, título, contenido, URLDrive."""

class Clases():
       def __init__(self, fecha, titulo, contenido, URLDrive)->None:
              self.fecha = fecha
              self.titulo = titulo
              self.contenido = contenido
              self.URLDrive = URLDrive

              






cur = Curos1("22/15/2023", "base de datos", "mysql", "aprender a hacer un crud", "mysque workbench", 5500, "foto.jpg", 8, "no", 3)


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
print(docent)

"""Por otra parte, los interesados en inscribirse a un curso deberán crearse una cuenta de usuario
final, donde deberán registrar su datos personales (nombre, apellido, dni, dirección, fecha
nacimiento, dirección, localidad, código postal, provincia, teléfono celular, email)"""

class UsuarioInteresado():
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
              self.email =email





"""además de
confirmar y reconfirmar una clave de acceso. Para la activación de la cuenta de usuario final se
deberá validar que el email sea verdadero y esté en funcionamiento, enviando un correo
automático al email registrado."""


"""Los usuarios públicos registrados pueden inscribirse a uno o más cursos. Además, el sitio
deberá proveer la posibilidad de registrar 2 roles más de usuarios quienes también tendrán
interacción con el sistema: Administrador, Docente. Los usuarios también deben tener
asociado un estado (Activo / Inactivo)."""


"""Por último, los usuarios finales podrán agregar uno o más cursos en un carrito de compras,
donde se deberá visualizar: Foto, título del curso, duración, costo. Una vez confirmados los
ítems del carrito, deberá seleccionar el medio de pago, los cuales pueden ser: Tarjeta de
crédito/débito y transferencia bancaria; a fin de tener más datos acerca de los medios de
pago, deberán registrarse los datos básicos de tarjetas y transferencias). Al confirmar la
compra, se deberá registrar además la fecha de compra, el usuario que realiza la compra y el
monto total. Dada la consigna anterior, se pide: identificar, analizar y documentar los
requisitos según el formato de historias de usuario. Para la creación de las historias, hacer uso
del repositorio Github, a través de creación de issues."""