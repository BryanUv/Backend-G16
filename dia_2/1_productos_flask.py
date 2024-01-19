from flask import Flask, request
from uuid import uuid4
from flask_cors import CORS

app = Flask(__name__)

CORS(
    app=app, 
    # que metodos pueden accdeder a mi api
    methods=['GET','POST','PUT','DELETE'], 
    # desde que dominios se pueden acceder a mi api, si queremos que cualquier origen se conecte colocamos el *
    origins=['http://localhost:5500', 'http://127.0.0.1:5500'],
    #que headers(cabeceras) pueden enviar a mi api , *
    allow_headers=['accept','authorization', 'content-type'] 
    )

productos = [
  {
    'id': uuid4(),
    'nombre':'Palta fuerte',
    'precio':7.50,
    'disponibilidad':True
  },
  {
    'id': uuid4(),
    'nombre':'Lechuga Carola',
    'precio':1.50,
    'disponibilidad':True
  }
]

@app.route('/', methods=['GET'])
def inicio():
  return{
    'message':'Bienvenido a la API de Productos'
  },200

@app.route('/productos', methods=['GET'])
def gestionProductos():
  return{
    'message':'Los productos son',
    'content':productos
  },200

# si voy a recibir un parametro dinamico (que va a cambiar su valor) y eso lo voy a manejar internamente
# los formatos que puedo parsear son:
# string > para recibir solo numeros
# floar > para recibir numeros con punto decimal
# path > que son string pero tmb aceptan slashes
# uuid > aceptar UUID's
# al colocar un parseador si el formato que envia el cliente no cumple con este conversion no aceptara la peticion

@app.route('/producto/<uuid:id>', methods=['GET'])
def gestionProducto(id):
  print(id)
  # tenemos una lista de productos en el cual en cada posicion tenemos un diccionario y una llave llamada id
  # iteren esos productos y vean si existe el producto con determinado id
  # si no existe entonces retornar un mensaje que dia 'Producto no existe' con un estado 404
  # PISTA: hacer un for con if y else dentro de el
  for producto in productos:
    if producto['id'] == id:
      return{
        'content':producto
      },200
  return{
    'message':'El producto no existe'
  },404

@app.route('/producto', methods=['POST'])
def crearProducto():
  # convierte la data del body a un dictionary si el body es un JSON
  data = request.get_json()
  # antes de guardar 
  data['id']=uuid4()

  productos.append(data)
  return{
    'message':'Producto creado exitosamente',
    'content': data
  },201 #created

if __name__ == '__main__':
  app.run(debug=True)