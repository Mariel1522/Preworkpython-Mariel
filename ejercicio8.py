#Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona

peso = float(input('Escriba su peso (kg):'))
estatura = float(input('Escriba su estatura (m): '))
IMC = round(float(peso)/ float(estatura)**2,2) 

print("Tu indice de masa corporal es" + str(IMC))
