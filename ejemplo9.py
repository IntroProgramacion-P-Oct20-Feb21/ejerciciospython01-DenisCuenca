"""
    Ejemplo 05
    Uso del ciclo for
"""
# Ingreso de datos por teclado
tabla = int(input("Ingrese la tabla a generar: "))
limite = int(input("Ingrese el límite de la tabla: "))

# uso ciclo repetitivo for
for i in range(1, limite+1):
    valor = tabla * i
    print("%d * %d = %d" %(tabla, i, valor))
