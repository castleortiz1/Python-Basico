def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicacion(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: División por cero"

# Solicitar entrada al usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

operacion = input("Seleccione la operación (+, -, *, /): ")

if operacion == '+':
    print(suma(num1, num2))
elif operacion == '-':
    print(resta(num1, num2))
elif operacion == '*':
    print(multiplicacion(num1, num2))
elif operacion == '/':
    print(division(num1, num2))
else:
    print("Operación no válida")
