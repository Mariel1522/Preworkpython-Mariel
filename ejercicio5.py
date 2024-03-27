#Escribe un programa que calcule la suma de todos los números pares del 1 al 100
suma = 0
c = 0
for x in range(1,101,1):
  if x % 2 ==0:
     print(x)
     suma = suma + x
     c = c + 1
print("El total de nuemros pares es:", c)
print("La suma de los numero pares es:",suma)
