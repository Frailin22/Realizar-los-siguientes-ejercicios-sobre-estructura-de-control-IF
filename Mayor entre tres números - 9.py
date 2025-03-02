# Pedir al usuario tres números
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

if num1 == num2 == num3:
    print("Los tres números son iguales.")

elif num1 >= num2 and num1 >= num3:
    print(f"El número mayor es: {num1}")
    if num1 == num2 or num1 == num3:
        print("Hay dos números iguales que son los mayores.")

elif num2 >= num1 and num2 >= num3:
    print(f"El número mayor es: {num2}")
    if num2 == num1 or num2 == num3:
        print("Hay dos números iguales que son los mayores.")

elif num3 >= num1 and num3 >= num2:
    print(f"El número mayor es: {num3}")
    if num3 == num1 or num3 == num2:
        print("Hay dos números iguales que son los mayores.")
