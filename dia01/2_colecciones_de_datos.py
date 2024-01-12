# puedo agrupar varios valores en una variable

# Listas
# se puede modificar, ordenada por indices
alumnos = ['victor', 'hiroito', 'marco', 'angel', 'bryan', 'samael', 'claudia']

# las listas empiezan con la posicion 0
print(alumnos[0])
print(alumnos[4])

# para saber el contenido (longitud) de datos
# cuenta y no utiliza las posiciones
print(len(alumnos))

# si queremos recorrer la lista de derecha a izq utilizamos numeros negativos
print(alumnos[-1])

print(alumnos[len(alumnos)-1])

# agregar elementos a una lista ya creada
alumnos.append('franklin')
print(alumnos)

# remover un elemento de la lista lo podemos guardar en una variable
alumno_eliminado = alumnos.pop(3)
print(alumnos)
print(alumno_eliminado)

# del > podemos eliminar variables, posiciones de la lista y otras cosas
del alumnos[0]
print(alumnos)
# cada vez que se elimina una posicion de la lista, todas las demas posiciones ocupan ese lugar disponible

# modificar el valor de una posicion en la lista
alumnos[0] = 'eduardo'

# limpiar toda la lista y la dejamos vacia
alumnos.clear()
print(alumnos)

# las listas pueden contener varios tipos de datos
mixto = ['lunes', 10, False, 80.5, [1,2,3]]

print(mixto[4][2])

ejercicio = [1,2,3, [4,5,6]]

# Devolver el valor de 3
print(ejercicio[2])
# Como puedo devolver el valor de 5
print(ejercicio[3][1])

# tuplas
# no se puede modificar y es ordenada (indices)
# se usa para guardar valores que jamas van a poder cambiar

meses = ('enero', 'febrero', 'marzo', 'abril')

print(meses[0])


data = ('juan', 'roberto', [1,2,3, ['eduardo', 'frank']])
# obtener eduardo
print(data[2][3][0])

# set(conjuntos)
# desordenada y modificable
colores = {'negro', 'blanco', 'guinda', 'violeta'}
print(colores)
colores.add('azul')
print(colores)

print('verde' in colores)

colores.remove('blanco')
print(colores)

# Diccionarios
# ordenados pero por llaves y modificables
persona = {
  'nombre': 'eduardo',
  'edad': 31,
  'nacionalidad': 'peruano',
  'apellido': 'de rivero'
}

print(persona.keys())
print(persona.values())
print(persona['edad'])

persona['nombre'] = 'juancito'
persona['calzado'] = 'zapatos'
print(persona)

persona = {
    'nombre':"Roberto",
    'edad': 40,
    'hobbies': ['Nada', 'Pescar', 'Jugar videojuegos'],
    'idiomas': [
        {
            'nombre': 'Ingles',
            'nivel': 'Intermedio'
        },
        {
            'nombre': 'Frances',
            'nivel': 'Basico'
        }
    ],
    'habilidades': {'Puntual', 'Economico', 'Proactivo'},
    'debilidades': ('Mentiroso', 'Resentido', 'Comelon')
}

# 1.darme la edad
print(persona['edad'])

# 2.mostrar los hobbies
print(persona['hobbies'])

# 3.mostrar el ultimo hobbie ingresado
print(persona['hobbies'][-1])

# 4.mostrar los idiomas SOLO SUS NOMBRES
print(persona['idiomas'][0]['nombre'])
print(persona['idiomas'][1]['nombre'])

# 5.Ver si es proactivo > true o false
print('Proactivo' in persona['habilidades'])

# 6.ver cuantas debilidades tiene (cantidad)
print(len(persona['debilidades']))