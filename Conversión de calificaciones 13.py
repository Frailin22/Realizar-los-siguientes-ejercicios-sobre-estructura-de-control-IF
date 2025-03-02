# Este programa convierte las calificaciones en letra.
calificacion = float(input("Ingresa la calificación del estudiante (0-100): "))

if 90 <= calificacion <= 100:
    print("La calificación es A.")
elif 80 <= calificacion < 90:
    print("La calificación es B.")
elif 70 <= calificacion < 80:
    print("La calificación es C.")
elif 60 <= calificacion < 70:
    print("La calificación es D.")
elif 0 <= calificacion < 60:
    print("La calificación es F.")
else:
    print("Calificación fuera de rango. Debe estar entre 0 y 100.")
