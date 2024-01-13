# def > funciones
# funcion puede o no recibir parametros
# funcion puede o no retornar algo
def saludar():
  print('Buenas noches!')

# si la funcion esta definida pero no esta implementada el codigo dentro de la funcion nunca se ejecutara
saludar()

def sumar(numero1, numero2):
  resultado = numero1 + numero2
  print('la sumna es ', resultado)

sumar(10, 20)

def multiplicar(numero1, numero2):
  resultado = numero1 * numero2
  return resultado

resultado_multiplicacion = multiplicar(50,20)
print(resultado_multiplicacion)

# si queremos colocar parametros por defecto entonces debemos colocarlo al final
def saludarCordialmente(nombre, cargo='Siñorsh'):
  return 'Buenas noches {} {}'.format(cargo, nombre)

print(saludarCordialmente('juancito'))
print(saludarCordialmente('Sofia', 'Damicela'))

print(saludarCordialmente(cargo='Gerente',nombre='Raul'))

# el * el momento de definir una funcion indicaremos que esta puede recibir n valores
def sumarNumeros(*args):
  resultado = 0
  # devolver la sumatoria de todos los valores que recibe args
  for numero in args:
    resultado += numero
  return resultado

resultado = sumarNumeros(10,20,30,40,50,60,70,80,90,110)
print(resultado)

# ** sirve para recibir un numero ilimitado de parametros
# kwargs > keyboard arguments
def capturarPersona(**kwargs):
  return kwargs

resultado = capturarPersona(nombre='eduardo', 
                            apellido='de rivero',
                            correo='edirivero@gmail.com', 
                            estatura='1.87')

print(resultado)

data = {
  'nombre':'eduardo',
  'apellido':'de rivero',
  'correo':'asdagmail.com',
  'estatura':1.87
}
# el metodo get solo sirve para devolver informacion mas no para asignar nuevos valores
print(data.get('apellido'))
data['edad']= 30
