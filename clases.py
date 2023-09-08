import re
import datetime

from validate_email_address import validate_email


"""Por cada curso se deberá visualizar la fecha de comienzo, título, descripción, objetivos,
programa, costo, duración en meses, foto y estado (disponible o no disponible, en base a su
estado deberán verse o no en el sitio) <---datos, atributos). 

A su vez, cada curso pertenece a alguna de las
siguientes categorías (Inicial, Intermedio, Avanzado)<---metodos."""


listadeclasess = []
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
          return f"Hola bienvenido al curso de {self.titulo} \nel mismo comieza el dia {self.fecha}\nen el veremos {self.descripcion}\nnuestro objetivo es que {self.objetivos}\nnuestro programa es {self.programa}\nel curso tiene un valor de {self.costo}\ntu foto de perfil es {self.foto}\nel mismo tiene una duracion de {self.duracion_meses} mesess"
    
       def estado_del_curso(self): #metodo disponibilidad
                if self.estado == "disponible":
                        print("el curso  esta disponible")
                else:
                        print("el curso no esta disponible")
       def categoriaCurso(self):
               if self.categoria == 1:
                      print("inicial")
               elif self.categoria == 2:
                      print ("intermedio")
               else:
                      print ("avanzado")
       def agregarClases(self, a):
              listadeclasess.append(a)
              print("se agrego la clase", a.titulo ,"tu curso")
       
       def verclases(self):
              for i in listadeclasess:
                     print(i)
        
"""Por otro lado, los cursos contienen un conjunto de clases,
en donde por cada clase se debe
mostrar la fecha, título, contenido, URLDrive."""



class Clases():
        
       def __init__(self, fecha, titulo, contenido, URLDrive):
              self.fecha = fecha
              self.titulo = titulo
              self.contenido = contenido
              self.URLDrive = URLDrive
       def __str__(self)->str:
              return f"Fecha de la clase {self.fecha}, Titulo {self.titulo}, El contenido {self.contenido}, Link del Drive {self.URLDrive}"

der = Clases("22/09/2023", "DER", "virtual", "www.drive.com")









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
       




"""Por otra parte, los interesados en inscribirse a un curso deberán crearse una cuenta de usuario
final, donde deberán registrar su datos personales (nombre, apellido, dni, dirección, fecha
nacimiento, dirección, localidad, código postal, provincia, teléfono celular, email) además de
confirmar y reconfirmar una clave de acceso. Para la activación de la cuenta de usuario final se
deberá validar que el email sea verdadero y esté en funcionamiento, enviando un correo
automático al email registrado."""
listaDeCursos = []
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
              
       def __str__(self)->str:
              return f"DATOS DEL USUARIO\nApellido {self.apellido}\nNombre {self.nombre}\nDNI {self.dni}\nNacimiento {self.nacimiento}\nDireccion {self.direccion}\nLocalidad {self.localidad}\nCodigo Postal {self.codigo_postal}\nProvincia {self.provincia}\ntelefono celular {self.celular}\nEmail {self.email}"
       def get_apellido(self):
              return self.apellido
       def get_nombre(self):
              return self.nombre
       def get_dni(self):
              return self.dni
       def get_email(self):
              return self.email


       def validacion(self):
                            
                     if validate_email(self.email) == True and not re.match(r"[^@]+@[^@]+\.[^@]+", self.email) == False:
                            
                            print("su direccion de correo electronico es valido")
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
                                   print("corrabore sus datos y vuelva a intentar")
                     else:
                            print("correo no valido")
       def agregarCurso(self, a):
              listaDeCursos.append(a)
              print("se agrego curso", a.titulo)
       








class Administrador():
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
              return f"DATOS DEL ADMINISTRADOR\nApellido {self.apellido}\nNombre {self.nombre}\nDNI {self.dni}\nNacimiento {self.nacimiento}\nDireccion {self.direccion}\nLocalidad {self.localidad}\nCodigo Postal {self.codigo_postal}\nProvincia {self.provincia}\ntelefono celular {self.celular}\nEmail {self.email}"


"""Los usuarios públicos registrados pueden inscribirse a uno o más cursos. Además, el sitio
deberá proveer la posibilidad de registrar 2 roles más de usuarios quienes también tendrán
interacción con el sistema: Administrador, Docente. Los usuarios también deben tener
asociado un estado (Activo / Inactivo)."""

class Usuarios():
       
       def rol(self,a,b):
              rol = int(input("si desea incribirse como docente presione 1 ""\n""si desesa incribirse como administrador presione 2 "))
              if rol == 1:
                  
                     print(f"Bienvenido profe {a.nombre} continuacion corrboraremos sus datos para crear su usario al curso")
                     input("verifique sus datos a continuacion, presiones enter")
                     print(a)
                     correcion = int(input("Si sus datos son correcto presione 1, si no presione 2 "))
                     if correcion == 1:
                            generar = input("Genere su contraseña, recuerde que ambas deben coincidir, presione enter para continuar")
                            while True:
                                   clave1 = input("Ingrese una clave por favor: ")
                                   clave2=input ("Repita la clave para confirmarla: ")
                                   if clave1==clave2:
                                          print(f"Se a enviado un correo automatico a {a.email} para su validacion")
                                          print("Una vez validada ya podra interactuar con el curos")
                                          break
                                   else:
                                          print("no coinciden las contraseñas vuelva a intentar ")
              elif rol == 2:
                     print(f"Bienvenido {b.nombre} como administrado, a continuacion corraboraremos sus datos para crear su usasrio")
                     input("verifique sus datos a continuacion, presiones enter")
                     print(b)
                     correcion = int(input("Si sus datos son correcto presione 1, si presione 2 "))
                     if correcion == 1:
                            generar = input("Genere su contraseña, recuerde que ambas deben coincidir, presione enter para continuar")
                            while True:
                                   clave1 = input("Ingrese una clave por favor: ")
                                   clave2=input ("Repita la clave para confirmarla: ")
                                   if clave1==clave2:
                                          print(f"Se a enviado un correo automatico a {b.email} para su validacion")
                                          print("Una vez validada ya podra interactuar con el curos")
                                          break
                                   else:
                                          print("no coinciden las contraseñas vuelva a intentar ")





"""Por último, los usuarios finales podrán agregar uno o más cursos en un carrito de compras,
donde se deberá visualizar: Foto, título del curso, duración, costo.
Una vez confirmados los ítems del carrito, 

deberá seleccionar el medio de pago, los cuales pueden ser: Tarjeta de
crédito/débito y transferencia bancaria; 

a fin de tener más datos acerca de los medios de
pago, deberán registrarse los datos básicos de tarjetas y transferencias).
Al confirmar la
compra, se deberá registrar además la fecha de compra, el usuario que realiza la compra y el
monto total."""

listaDeCurso = []
class Carrito():
             
              def __init__(self, a):
                     
                     print(f"-----Usted eligio el curso de: \n{a.titulo}\nFoto{a.foto}\nDuracion {a.duracion_meses}\nCon un costo de {a.costo} pesos")
                     res = input(f"desea agregar {a.titulo} al carrito de compras? digite si ")
                     if res == "si":
                            listaDeCurso.append(a)
                            print("se agrego ", a.titulo)
              
              
class Pagos():
       def __init__(self)->None:
                     self.resultado = 0
                     for i in listaDeCurso:
                            self.resultado += i.costo
                     print(f"el total a pagar es de {self.resultado}")
       def verCursos(self):
                    print("-----Sus cursos------")
                    for i in listaDeCurso:
                           print(f"Curso de {i.titulo}")
       def mediosPagos(self, a):
              pagos = int(input("Si desea pagar con tarjeta de credito digite 1\nsi desea pagar con tarjeta de debito digite 2\nsi desea pagar con tranferencia bancaria digite 3\n"))
              if pagos == 1:
                     recargo = self.resultado * 10 / 100
                     total = recargo + self.resultado
                     print("Usted a elegido tarjeta de credito, tiene un recargo de el 10 por ciento el total es: ", total)
                     print("")
                     nombreusuario = a
                     numeroTarjeta = int(input("Ingrese el numero de tarjeta por favor"))
                     nombreTitular = input("Ingrese el nombre que figura en al tarjeta")
                     codigo = int(input("ingrese el codigo de seguridad que figura al dorso de la tarjeta"))
                     cantidad = len(listaDeCurso)
                     fecha = datetime.datetime.now()
                     print("")
                     print(f"Nombre del usuario: {a.nombre}          fecha: {fecha}\nNumero de tarjeta: {numeroTarjeta}\nNombre del titular de la tarjeta {nombreTitular}\nEl codigo es: {codigo}\nPara la compra de {cantidad} cursos por el monto de {total}")

                     correcto = int(input("desea confirmar digite 1: "))
                     if correcto == 1:
                            print("Compra exitosa, se a enviado la factura a su correo electronico ", a)


              elif pagos == 2:
                     print("El precio es ", self.resultado)
                     print("Usted a elegido tarjeta de debito")
                     print("")
                     nombreusuario = a
                     numeroTarjeta = int(input("Ingrese el numero de tarjeta por favor"))
                     nombreTitular = input("Ingrese el nombre que figura en al tarjeta")
                     codigo = int(input("ingrese el codigo de seguridad que figura al dorso de la tarjeta"))
                     cantidad = len(listaDeCurso)
                     fecha = datetime.datetime.now()
                     print("")
                     print(f"Nombre del usuario: {a.nombre}          fecha: {fecha}\nNumero de tarjeta: {numeroTarjeta}\nNombre del titular de la tarjeta {nombreTitular}\nEl codigo es: {codigo}\nPara la compra de {cantidad} cursos por el monto de {self.resultado}")

                     correcto = int(input("desea confirmar digite 1: "))
                     if correcto == 1:
                            print("Compra exitosa, se a enviado la factura a su correo electronico ", a)
              else:
                     fecha = datetime.datetime.now()
                     cantidad = len(listaDeCurso)
                     print("El precio es ", self.resultado)
                     print("Usted a elegido tranferencia")
                     print(f"Nombre del usuario: {a.nombre}          fecha: {fecha}\nNumero de la compra de {cantidad} cursos por el monto de {self.resultado}")
                     print(f"El alias es CursosOnline, una vez que alla realizado la tranferencia enviarnos el comprobante de pago al email cursosonlines@hotmail.com\nEl impacto del mismo puede demorara 24 hs\nLuego se le enviara un email a {a.email} para confirmar su compra")
#-------------------------------------------------------------------------------------------------------------
