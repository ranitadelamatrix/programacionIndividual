from clases import *
print("**************************************")
print("*                                    *")
print("*        ¡Bienvenido a tu curso!     *")
print("*                                    *")
print("*                                    *")
print("**************************************")
print("")

baseDeDatos = Curos1("28/09/202", "Base de datos", "veremos crud", "conseguir trabajo", "numero 1", 6500, "foto.jpg", 5, "disponible", 1)
matematicas = Curos1("28/09/202", "logaritmo", "veremos sumas", "conseguir trabajo", "numero 1", 8000, "foto.jpg", 5, "disponible", 1)
print(baseDeDatos)
input("presiones enter para continuar viendo el codigo")
baseDeDatos.estado_del_curso()
baseDeDatos.agregarClases(der)
input("presiones enter para continuar viendo el codigo")

baseDeDatos.categoriaCurso()
input("presiones enter para continuar viendo el codigo")

baseDeDatos.verclases()
input("presiones enter para continuar viendo el codigo")

print("")
kevin = Docente("ksler", "kevin", 33669317, "02/06/1988", "catamarca 2660", "villa maria", 5900, "cordoba", 385417268, "kkvin@hotmail.com")
print(kevin)
print("")
input("presiones enter para continuar viendo el codigo")

gaston = RegistrarUsuario("gaston", "trejo", 33693177, "catamarca", "02/06/1988", "villa maria", 5900, "cordoba", 3854172687, "gastontrejo9099@hotmail.com")
print(gaston)
input("presiones enter para continuar viendo el codigo")

gaston.validacion()
input("presiones enter para continuar viendo el codigo")

gaston.agregarCurso(baseDeDatos)
print("")
input("presiones enter para continuar viendo el codigo")

cesaradmin = Administrador("martins", "cesar", 378889, "29/02/1990", "docta", "cordoba capital", 5000, "cordoba", 3512222, "cesarecrack@hotmail.com")
adminProfe = Usuarios()
adminProfe.rol(kevin, cesaradmin)
input("presiones enter para continuar viendo el codigo")

print("")
carrito1 = Carrito(baseDeDatos)
carrito2 = Carrito(matematicas)
input("presiones enter para continuar viendo el codigo")

print("")
compra = Pagos()
compra.verCursos()
compra.mediosPagos(gaston)
