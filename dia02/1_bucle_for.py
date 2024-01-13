alumnos = ['angel', 'bryan', 'carlos', 'hiroito', 'claudia', 'samael', 'marco']

for alumno in alumnos:
  print(alumno)

# for se puede utilizar con string (textos)
frase = 'No hay mal que por bien no venga'

for letra in frase:
  # print(letra)
  # imprimir el texto pero sin espacios
  # pista: usar el if y el pass
  # pista: usar el if sin el else

  # forma 1
  # if letra == ' ':
  #   pass
  # else:
  #   print(letra)

  # forma 2
  # if letra != ' ':
  #   print(letra)

  # forma 3
  # continue > termina el ciclo actual (la iteracion en camino) y no permite hacer nada mas luego del continue
  # continue solo se puede utilizar dentro de un loop (for, while)
  if letra == ' ':
    continue
  print(letra)

  None if letra == ' ' else print(letra)

# range > si quiero realizar un for manual si uso de listas, tuplas, set o textos
# for i in range(4,8,2):
#   print(i)

for numero in range(4):
  print(numero)

print('-----------------')

for numero in range(1, 4):
  print(numero)

print('-----------------')

for numero in range(1, 10, 2):
  print(numero)

# 
texto = 'Hola me llamo eduardo'
vocales = ['a', 'e', 'i', 'o', 'u']

print('j' in vocales)
print('e' in vocales)

# iterar la variable texto y ver cuantas vocales hay
# respuesta: hay 9 vocales

c = 0
for letra in texto:
  if letra != ' ':
    if letra in vocales:
      c += 1
print('Hay', c , 'Vocales')
print('Respuesta: %s  vocales %s' % (c, 80))
print('hay {} vocales'.format(c))
print(f'hay {c} vocales')

# %
print(99/5) #cociente
print(99% 5) # residuo entero
print(99 // 5 ) # cociente entero sin el uso de decimales

n = 9

if n % 2 == 0:
  print(n, "es par.")
else:
  print(n, "es impar.")

range(1, 56)
# quiero saber cuantos numeros pares tengo
# resultado: hay 27 numeros pares
numero % 2 == 0 #es numero par

co = 0
for par in range(1, 56):
  if par % 2 == 0:
    co += 1
print(f'Hay: {co} pares')