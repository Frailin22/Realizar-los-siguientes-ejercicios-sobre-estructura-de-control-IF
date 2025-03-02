# Este programa solicita la calificación de un estudiante (0-100) y determina si aprobó (mínimo 60) o reprobó.

Calificación = int(input("Por favor ingrese la calificacion del estudiante: "))

if Calificación >= 60:
    print("¡Felicidades! usted aprobo. ")
elif Calificación < 0 and Calificación < 60:
    print ("esfuercese más, usted a reprobado. ")
else:
    print("Error en la calificacion ingresada. ")
