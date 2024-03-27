#Escribe un programa que convierta un número de minutos en horas y minutos. Por ejemplo, 145 minutos serían 2 horas y 25 minutos.
dato = int(input("Ingrese los minutos,"))
hora = dato// 60
minuto = dato % 60
print("Horas:", hora, "minutos:", minuto)