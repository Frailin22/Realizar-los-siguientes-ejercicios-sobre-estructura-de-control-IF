# Este programa define si la temperatura.

temperatura = float(input("Ingresa la temperatura en grados Celsius: "))
if temperatura < 0:
    print("Hace mucho frío")
elif 0 <= temperatura <= 20:
    print("Clima fresco")
elif 21 <= temperatura <= 30:
    print("Clima agradable")
else:
    print("Hace mucho calor")
