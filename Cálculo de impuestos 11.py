# Pedir al usuario su salario mensual
salario = float(input("Ingresa tu salario mensual: "))

if salario < 10000:
    impuesto = 0
elif salario <= 30000:
    impuesto = salario * 0.10 
else:
    impuesto = salario * 0.20

salario_neto = salario - impuesto
print(f"Tu impuesto a pagar es: ${impuesto:.2f}")
print(f"Tu salario después de impuestos es: ${salario_neto:.2f}")
