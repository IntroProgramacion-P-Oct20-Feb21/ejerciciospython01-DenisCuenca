"""
    Ejemplo 05
    Uso del ciclo for
"""
# Ingreso de datos por teclado
tabla = int(input("Ingrese hasta que número de tabla desea generar: "))
limite = int(input("Ingrese el límite de cada tabla: "))

# uso ciclo repetitivo for con un for interno
for i in range(1, tabla+1):
    print("Tabla del número %s" % (i))
    for j in range(1, limite+1):
        valor = i * j
        print("%d * %d = %d" %(i, j, valor))
    print()
