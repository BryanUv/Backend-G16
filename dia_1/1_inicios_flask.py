from flask import Flask, request

# __name__ > variable python que sirve para indicar si el archivo que estamos utilizamos es el archivo principal del
# proyecto esto sirve para que la instancia del flask solamente corra en el archivo principal y asi
# evitar instancias de flask en archivos secundarios del proyecto

app = Flask(__name__) # es el encargado de crear mi servidor del backend

# si el archivo es el archivo principal  el valor de __name__ sera __main__

# Decoradores
# Sirve para utilizar un metodo sin la necesita de modificarlo desde la calse en la cual estamos haciendo la
# referencia
# Get > devolver
# post > creaciones
# put > actualizar
# delete > eliminar
@app.route('/', methods=['GET','POST','PUT'])
def inicio():
  # request.method > devolvera el metodo por http que esta realizando el cliente
  if request.method == 'PUT':
    return {
      'message': 'Actualizacion exitosa'
    },202 # estado de respuesta http (ok)
  
  elif request.method == 'GET':
    return {
      'message': 'Devolucion exitosa'
    },200 #ok
  
  elif request.method == 'POST':
    return {
      'message': 'Creacion exitosa'
    },201 #created
  
  print(request.method)

  return{
    'message':'Bienvenido a mi primera API con flask',
    'content':'hola'
  }


# levantamos nuestro servidor de flask
app.run(debug=True)