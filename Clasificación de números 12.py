# Solicitar los tres números al usuario

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

if num1 > 0 and num2 > 0 and num3 > 0:
    print("Todos los números son positivos.")
elif num1 < 0 and num2 < 0 and num3 < 0:
    print("Todos los números son negativos.")
elif num1 == 0 or num2 == 0 or num3 == 0:
    print("Hay ceros en los números.")
else:
    print("Los números son mixtos.")
