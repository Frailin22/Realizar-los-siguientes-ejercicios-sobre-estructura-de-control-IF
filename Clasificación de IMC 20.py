# Solicitar el peso y la altura

peso = float(input("Ingresa el peso en kilogramos: "))
altura = float(input("Ingresa la altura en metros: "))

imc = peso / (altura ** 2)
if imc < 18.5:
    print(f"Tu IMC es {imc:.2f}. Bajo peso.")
elif 18.5 <= imc <= 24.9:
    print(f"Tu IMC es {imc:.2f}. Normal.")
elif 25 <= imc <= 29.9:
    print(f"Tu IMC es {imc:.2f}. Sobrepeso.")
else:
    print(f"Tu IMC es {imc:.2f}. Obesidad.")
