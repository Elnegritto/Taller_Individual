#EJERCICIO DE EXCEPCIONES (ValueError) 2

while True:
    try:
        numero = int(input("Digite un numero : "))
        print(13/numero)
        break
    except ValueError:  
        print("El valor no es correcto.")
         