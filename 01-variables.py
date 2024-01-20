nombre = "Juan" # string = cadena de texto
apellido = "medina" # string = cadena de texto
edad = 25 # integer es un numero entero
altura = 1.75 # float es un numero decimal 
verdadero = True # boleano
falso = False # boleano
# con todos estos datos podemos crear aplicaciones 

""" str: Cadenas de texto
    int: Números enteros
    float: Números de punto flotante
"""
print(nombre)
print(edad)
print(altura)
print(nombre + ' ' + apellido)

# Ejemplo de una variable local
def mi_funcion():
    numero = 10
    print(numero)

mi_funcion()

# Ejemplo de una variable global
numero_global = 20

def mi_funcion():
    print(numero_global)

mi_funcion()

# Ejemplo de una variable de clase
class MiClase:
    numero_clase = 30

mi_instancia = MiClase()
print(mi_instancia.numero_clase)
