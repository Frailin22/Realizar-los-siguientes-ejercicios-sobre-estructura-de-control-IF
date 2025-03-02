# Este programa determina si un año es bisiesto o no y si es divisible de algunos números.

anio = int(input("Ingresa un año: "))
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print(f"El año {anio} es bisiesto.")
else:
    print(f"El año {anio} no es bisiesto.")
