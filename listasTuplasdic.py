"""Crear cuatro listas:
1. Con los nombres de su familia.
2. Con los valores de la temperatura de un mes entero (mes a elección, pero definirlo).
3. Con los nombres de ciudades que hayan visitado.
4. Con las fechas y nombres de eventos importantes de su vida."""

familia = ["dayana", "rebeca","gaston", "rene" , "yolanda", "edelmira"]
temperaturaFebrero = [27,32,32,33,34,36,37,37,34,37,35,34,34,36,38,32,32,33,30,34,35,36,34,35,37,36,35,37]
ciudadesVisitadas = ["merlo", "rio 3º", "rio 1º", "fernandez", "santiago del estero", "rosario","cañada de gomez", "Carlos paz", "La falda", "Valle hermoso", "Cosquin"]
eventosImportantes = ["12/09/2016", "nacimiento de Rebeca", "24/12/2017", "Mi casamiento", "29/09/2017", "compramos la casa"]

"""1. Ordenar alfabéticamente la lista de los nombres de familia.
2. Ordenar ascendentemente la lista de temperaturas.
3. Agregar en la lista de temperaturas, las temperaturas de los 15 días del mes siguiente.
4. Quitar de la lista de los nombres de familia, a tus abuelos.
5. Quitar de la lista de ciudades la ciudad menos linda que hayas visitado.
6. Mostrar todas las listas."""

familia.sort()
temperaturaFebrero.sort()
temperaturaMarzo = [36,37,38,36,35,34,35,32,34,35,36,36,35,32,32]
temperaturaTotal = temperaturaFebrero + temperaturaMarzo
tempOtraOpcion = [temperaturaFebrero, temperaturaMarzo] #otra opcion tipo matriz
familia.remove("edelmira")
del familia[3:5]
ciudadesVisitadas.remove("rio 1º")
print(familia)
print(temperaturaFebrero)
print(temperaturaTotal)
print(ciudadesVisitadas)
print(eventosImportantes)
print(tempOtraOpcion)

"""Crear tres tuplas con datos random.
Crear una lista que las contenga y mostrarla."""

locomotoras = (9099, 9100, 9022, 9090, 6617, 6621, 8287, 8280, 8282)
basesRelevo = ("villa maria", "ferreyra", "cañada de gomez", "rio 3º", "rio 1º", "general deheza")
coloresPrimarios = ("rojo", "azul", "amarillo")

listaDeTupas = [locomotoras, basesRelevo, coloresPrimarios]
print(listaDeTupas)

"""Crear el siguiente diccionario:
 Las claves serán los dni de su núcleo familiar, y el valor será SOLO el nombre de la persona.
Luego deberán añadir los datos de familia ampliada (abuelos, familia política, etc)
 Crear un nuevo diccionario con claves autogeneradas y valores de números de teléfono.
Ambos deben ser mostrados."""

datosFamilia = {33693168: "trexo gaston", 37443871: "dayana palomino", 55599456: "trexo rebec"}
datosFamilia[33225566] = "trexo rene"
datosFamilia[3325557] = "ferreyra lito"
datosFamilia[3329986] = "silva fito"
datosFamilia[33754216] = "gomez juan"

numerosTelefonicos = {1: 35366884, 2: 35344788, 3: 3514788, 4: 35163398, 5: 3512314, 6: 35322244}

print(datosFamilia)
print(numerosTelefonicos)