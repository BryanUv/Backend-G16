# while puede convertirse en un bucle infinito

numero = 10
while numero < 20:
  print('hola')
  print(numero)
  numero += 1

# en python no existe el do-while
  
# valor = input('Por favor ingresa un numero: ')
# print(valor)

# Adivina el numero
numero = 75
numero_adivinado = 0

while numero_adivinado != numero:
  # todos los valores que le pasemos al input se capturaran con string
  numero_adivinado = int(input('Por favor ingresa un numero: '))