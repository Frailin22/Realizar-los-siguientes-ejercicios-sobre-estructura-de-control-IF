# Este programa pide un número y determina si es multipli de 5

num = int(input("Escbriba un número: "))
if num % 5 == 0:
    print("El número es múltiplo de 5.")
elif num % 5 != 0:
    print("El número NO es múltiplo de 5.")
else:
    print("Error en la entrada.") 