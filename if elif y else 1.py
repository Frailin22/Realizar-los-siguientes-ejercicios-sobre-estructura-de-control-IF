# Solicitar un número al usuario y determina si es positivo o negrativo.

num = float(input("Ingresa un número: "))

# Determinar si es positivo, negativo o cero
if num > 0:
    print("El número es positivo.")
elif num < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")
