import datetime

def convertir_temperatura(escala, temperatura):
    """
    Convierte una temperatura de una escala a otra.

    Args:
        escala: La escala de temperatura original.
        temperatura: La temperatura en la escala original.

    Returns:
        La temperatura en la escala de destino.
    """

    if escala == "celsius":
        if temperatura < -273.15:
            return None
        return temperatura * 9 / 5 + 32
    elif escala == "fahrenheit":
        if temperatura < -459.67:
            return None
        return (temperatura - 32) * 5 / 9
    elif escala == "kelvin":
        return temperatura
    else:
        return None


def main():
    # Solicitar la escala de temperatura
    escala = input("Elija la escala de temperatura original (celsius, fahrenheit o kelvin): ")

    # Solicitar la temperatura
    temperatura = float(input("Ingrese la temperatura: "))

    # Convertir la temperatura
    temperatura_convertida = convertir_temperatura(escala, temperatura)

    # Guardar la conversión en un archivo
    fecha = datetime.datetime.now()
    with open("banco/conversiones.txt", "a") as archivo:
        archivo.write(f"{fecha} - {escala}: {temperatura} - {temperatura_convertida} - {temperatura_convertida + 273.15}\n")


if __name__ == "__main__":
    main()
