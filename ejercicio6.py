#Crea un programa que verifique si una palabra ingresada por el usuario es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda)

word = input("Escribe una palabra:")
reversed_word = word
word = list(word)
reversed_word = list(reversed_word)
reversed_word.reverse()
if word == reversed_word:
  print("Es un palindromo")
else:
  print("No es un palindromo")
