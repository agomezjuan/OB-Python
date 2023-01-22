es_bisiesto = lambda anio: anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

year = int(input("Ingresa un año: "))
if es_bisiesto(year):
    print(year, "es un año bisiesto.")
else:
    print(year, "no es un año bisiesto.")
