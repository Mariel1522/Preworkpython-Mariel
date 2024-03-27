#Escribe un programa que determine si un número ingresado por el usuario es primo o no
n = int(input("Ingresa un numero:"))
x = 1
c = 0
while x <= n:
  if n % x ==0:
    c = c + 1
  x = x + 1
if c == 2:
  print ("El numero", n , "es primo")
else:
  print ("El numero", n, "no es primo")
