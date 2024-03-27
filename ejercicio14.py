#Crea un programa que calcule el precio final de un artículo después de aplicar un descuento del 20%.
inicio= int(input("Introdcue el precio del articulo: "))
descuento = 20 
finaldescuento  = inicio / 100 * descuento
precio = inicio - finaldescuento
print ("El precio final del articulo es: ",precio)

