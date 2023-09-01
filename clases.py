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
cur.ingresarClases("12/25/222", "crud", "musqjwe", "wwww")
