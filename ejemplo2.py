"""
    Ejemplo 02
    Ingreso de datos por teclado
    Usar condicionales para obtener la calificacion cualitativa
    0-4.9 --- Regular
    5.0 - 6.9 -- Bueno
    7.0 - 8.9 -- Muy Bueno
    9.0 - 10 -- Sobresaliente
    mayor a 10.1 - Fuera de rango
"""

nombre = input("Ingrese nombre del persona: ")
edad = int(input("Ingrese edad de persona: "))
promedio = float(input("Ingrese promedio del estudiante: "))

# uso de condicionales, simples, compuestos, anidados
if promedio > 10.1 or promedio < 0:
    cadena = "Promedio fuera de rango"
else:
    if (promedio >= 9) and (promedio <=10):
        cadena = "Sobresaliente"
    else:
        if (promedio >= 7.0) and (promedio <=8.9):
            cadena = "Muy bueno"
        else:
            if (promedio >= 5.0) and (promedio <=6.9):
                cadena = "Bueno"
            else:
                if (promedio >= 0) and (promedio <=4.9):
                    cadena = "Regular"

mensajeFinal = "Datos del estudiante\n\tNombre:%s\n\tEdad:%d\n\tPromedio:%.2f "\
        "equivalente a %s\n" % (nombre, edad, promedio, cadena)

print(mensajeFinal)
