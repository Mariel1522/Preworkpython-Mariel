#Crea un programa que cuente la cantidad de palabras en una oración ingresada por el usuario.
oracion = input("Escriba una oracion:")
palabras = oracion.split()
print(len(palabras))