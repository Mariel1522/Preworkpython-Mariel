#Crea un programa que cuente y muestre la cantidad de números pares e impares en una lista ingresada por el usuario.

def contar_pares_impares(lista):
    pares, impares = 0, 0 
    for n in range:
        if n % 2==0:
             pares += 1
        else:
             impares += 1
    return pares, impares

numeros = range[1,100,1]
resultado = contar_pares_impares(numeros)
print("La cantidad de pares es: %i" % resultado[0])
print("La cantidad de impares es: %i" % resultado[1])
