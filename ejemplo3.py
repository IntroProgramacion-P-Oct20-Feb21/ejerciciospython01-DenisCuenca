"""
    Ejemplo 02
    Ingreso de información hasta que el usuario lo decida
"""

# inicializo variables
bandera = True
mensajeFinal = ""
# uso ciclo repetitivo while
while(bandera):
    nombre = input("Ingrese nombre del persona: ")
    edad = int(input("Ingrese edad de persona: "))
    mensajeFinal = "%sNombre: %s / Edad: %s\n" % (mensajeFinal, \
            nombre, edad)
    salir = input("Desea salir, ingrese si: ")
    if salir == "si":
        bandera = False
mensajeFinal = "Listado de Personas\n%s" % (mensajeFinal)
print(mensajeFinal)
