# if > si
edad = 20
nacionalidad = 'VENEZOLANO'

if edad > 18 and nacionalidad == 'PERUANO':
  print('Puedes votar')

# else > sino
else:
  print('Llamare a tus padres')

if edad > 18 or nacionalidad == 'PERUANO':
  print('Puedes votar')

# else > sino
else:
  print('Llamare a tus padres')

edad = 16

if edad > 18:
  print('Puedes votar')
elif edad > 15:
  print('Ya te falta poco para votar')
else:
  print('Que haces aqui?')

# Segun el sexo y la estatura hacer lo siguiente
# si es Masculino
    # si mide mas de 1.50 entonces indicar que no hay prendas
    # si mide entre 1.30 y 1.49 indicar que si hay ropa
    # si mide menos de 1.30 indicar que no hay prendas
# si es Femenino
    # si mide mas de 1.40 indicar que no hay prendas
    # si mide entre 1.10 y 1.49 indicar que si hay
    # si mide menos de 1.10 indicar que no hay

sexo = 'Masculino'
estatura = 1.35
# output > SI HAY ROPA

sexo = 'Masculino'
estatura = 1.80
# output > NO HAY ROPA

sexo = 'Femenino'
estatura = 1.20
# output > SI HAY ROPA

sexo = 'Femenino'
estatura = 1.08
# output > NO HAY ROPA

# if sexo == 'Masculino':
#   if estatura > 1.50:
#     print('No hay ropa')
#   elif estatura > 1.30 and estatura < 1.49:
#     print('Si hay ropa')
#   elif estatura < 1.30:
#     print('no hay')
# else:
#   if estatura > 1.40:
#     print('No hay ropa')
#   elif estatura > 1.10 and estatura < 1.49:
#     print('Si hay ropa')
#   elif estatura < 1.10:
#     print('no hay')

if sexo == 'Masculino':
  if estatura > 1.30 and estatura < 1.49:
    print('si hay ropa')
  else:
    print('no hay ropa')
else:
  # sexo = 'femenino'
  if estatura > 1.10 and estatura < 1.40:
    print('si hay ropa')
  else:
    print('no hay ropa')

# Operador Ternario
# condicion que sirve para ejecutarse en una sola linea y en base a la condicion retornara un valor u otro
nacionalidad = 'ECUATORIANO'

if nacionalidad == 'PERUANO':
  print('paga 5 soles')
else:
  print('paga 8soles')

#  resultado si es verdadero if condicional(es) else resultado si es false
resultado = 'pague 5 soles' if nacionalidad == 'PERUANO' else 'pague 8 soles'

print(resultado)