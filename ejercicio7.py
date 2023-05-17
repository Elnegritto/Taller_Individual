#EJERCICIO DE EXCEPCIONES (ZeroDivisionError) 1

while True:
    try:
        numero = int(input("Digite un numero : "))
        print(10/numero)
    except (ZeroDivisionError):
        print("Perdona no puedo dividir en 0. ")    
    