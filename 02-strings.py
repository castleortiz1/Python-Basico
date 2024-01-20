# texto es un objeto 
texto = "Hola Mundo"
# .upper es un motodo y el metodo es una funcion
print(texto.upper())
print(texto.lower())
# el metodo .find nos devuelve un indice 
print(texto.find("M")) 
nuevoTexto = texto.replace("Mun", "Pajarito Feliz")
print(texto, nuevoTexto)
# in nos devuelve un boolean verdadero o falso
print("Mundo" in texto)
