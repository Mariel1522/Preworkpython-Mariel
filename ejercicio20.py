#Crea un programa que sume todos los números en una lista ingresada por el usuario.
conteo = 5
datos = []
for i in range(conteo):
  numero = int(input('Introduce un numero: '))
  datos.append(numero)
total = sum(datos)
print(total)

