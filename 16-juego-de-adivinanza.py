import random

def juego_adivinanza():
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("Bienvenido al Juego de Adivinanza. Adivina el número entre 1 y 100.")

    while True:
        guess = int(input("Tu adivinanza: "))
        intentos += 1

        if guess == numero_secreto:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break
        elif guess < numero_secreto:
            print("Demasiado bajo. Intenta de nuevo.")
        else:
            print("Demasiado alto. Intenta de nuevo.")

# Iniciar el juego
juego_adivinanza()
