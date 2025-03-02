# Este programa solicita al usuario el valor de un ángulo en grados y determina si es agudo (<90°), recto (90°), obtuso (>90° y <180°) o llano (180°).

angulo = float(input("Ingresa el valor del ángulo en grados: "))

if angulo > 0 and angulo < 90:
    print("El ángulo es agudo (<90°).")
elif angulo == 90:
    print("El ángulo es recto (90°).")
elif angulo > 90 and angulo < 180:
    print("El ángulo es obtuso (>90° y <180°).")
elif angulo == 180:
    print("El ángulo es llano (180°).")
else:
    print("El valor ingresado no corresponde a un ángulo válido.")
