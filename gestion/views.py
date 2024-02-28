from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Plato, Ingrediente, Cheff
from .serializers import (PlatoSerializer, 
                          IngredienteSerializer, 
                          PreparacionSerializer,
                          PlatoConIngredientesYPreparacionesSerializer,
                          RegistroCheffSerializer)
from rest_framework import status
from os import remove
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.
def vistaPrueba(request):
  usuario = {
    'nombre':'Bryan',
    'apellido':'Urquizo',
    'hobbies':[
      {
        'descripcion': 'Ir al cine'
      },
      {
        'descripcion': 'Viajar'
      }
    ]
  }
  return render(request=request, template_name='prueba.html', context=usuario)

def mostrarRecetas(request):
  return render(request, 'mostrarRecetas.html')

# siempre en una funcion que trabaja como controlador recibiremos el request (informacion entrante del cliente)
@api_view(http_method_names=['GET', 'POST'])
def controladorInicial(resquest):
  return Response(data={
    'message': 'Bienvenido a mi API'
  })

class PlatosController(APIView):
  def get(self, request):
    # SELECT * from platos
    resultado = Plato.objects.all()
    print(resultado)
    # instance > cuando tenemos instancias del modelo para serializar
    # data > cuando tenemos informacion que vamos a guardar, modificar en la base de datos proveniente del cliente
    serializador = PlatoSerializer(instance=resultado, many = True)
    return Response(data={
      'message': 'Me hicieron get',
      'content': serializador.data
    })
  
  def post(self, request):
    print(request.data)
    serializador = PlatoSerializer(data=request.data)
    # valida si la informacion enviada por el cliente es correcta o no, devolvera un boolean
    validacion = serializador.is_valid()
    if validacion:
      # el serializador al momento de vincularlo con un modelo se crean metodos para guardar(save) y actualizar(update)
      serializador.save()

      return Response(data={
        'message':'Plato creado exitosamente'
      }, status=status.HTTP_201_CREATED)
    else: 
      return Response(data={
        'message':'Error al crear el plato',
        'content': serializador.errors # errores al momento de hacer la validacion
      }, status=status.HTTP_400_BAD_REQUEST)
    
class PlatoController(APIView):
  def get(self, request, id):
    plato_encontrado = Plato.objects.filter(id = id).first()
    if not plato_encontrado:
      return Response(data={
        'message':'El plato no existe'
      }, status=status.HTTP_404_NOT_FOUND)
    
    # print(plato_encontrado.ingredientes.all())
    serializador = PlatoConIngredientesYPreparacionesSerializer(
      instance=plato_encontrado)
    return Response(data={
        'content':serializador.data
      })
  
  def put(self, request, id):
    plato_encontrado = Plato.objects.filter(id = id).first()
    if not plato_encontrado:
      return Response(data={
        'message':'El plato no existe'
      }, status=status.HTTP_404_NOT_FOUND)
    
    imagen_antigua = plato_encontrado.foto.path
    
    serializador = PlatoSerializer(data=request.data)
    # validated_data > informacion que ya fue revisada y aprobada. Para utilizarla tenemos que llamar al metodo is_valid
    if serializador.is_valid():
      # es un metodo que tambien se encuentra al momento de usar un modelserializer y sirve para actualizar sin mucho trabajo
      resultado = serializador.update(instance=plato_encontrado, 
                          validated_data=serializador.validated_data)
      #ya se actualizo mi registro en la base de datos
      
      # eliminamos el archivo que ya no vamos a necesitar de nuestro servidor
      remove(imagen_antigua)
      return Response(data={
        'message':'Plato actualizado exitosamente'
      })
    else:
      return Response(data={
        'message':'Error al actualizar el plato',
        'content': serializador.errors
      },status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, id):
    plato_encontrado = Plato.objects.filter(id = id).first()
    if not plato_encontrado:
      return Response(data={
        'message':'El plato no existe'
      }, status=status.HTTP_404_NOT_FOUND)
    
    imagen_antigua = plato_encontrado.foto.path
    # delete from platos where id = ......;
    Plato.objects.filter(id=id).delete()

    # eliminamos la imagen de nuestro servidor
    remove(imagen_antigua)

    return Response(data=None, status=status.HTTP_204_NO_CONTENT)
  
class IngredientesController(APIView):
  def post(self, request):
    # Validar la data con el serializador creado (IngredienteSerializer) y si es que no es correcta indicar que no lo es con un estado 400
    # Caso contrario crear el ingrediente y retornar el mensaje de exito
    serializador = IngredienteSerializer(data=request.data)
    validacion = serializador.is_valid()
    if validacion:
      serializador.save()
      return Response(data={
        'message':'Ingrediente agregado exitosamente',
        'content':serializador.data # nos devovera la inforamcion agregada a la base de datos
      }, status=status.HTTP_201_CREATED)
    else:
      return Response(data={
        'message':'Error al guardar el Ingrediente',
        'content':serializador.errors
      },status=status.HTTP_400_BAD_REQUEST)
    
@api_view(http_method_names=['GET'])
def listarIngredientesPlato(request, id):
  # buscar todos los ingredientes de un plato
  ingrediente_encontrado = Ingrediente.objects.filter(platoId = id).all()
  if not ingrediente_encontrado:
    return Response({
      'message':'El plato no tiene ingredientes'
    })
  
  else:
    serializador = IngredienteSerializer(
      instance=ingrediente_encontrado, many=True)
    return Response({
      'content': serializador.data
    })
  
@swagger_auto_schema(method='post', 
                      request_body=PreparacionSerializer, 
                      responses={
                        201: openapi.Response('respuesta exitosa', 
                                              examples={
                                                'application/json':{
                                                  'message':'Preparacion agregada con exitosamente al plato',
                                                  'content':{
                                                    'id':1,
                                                    'descripcion':'',
                                                    'orden':1,
                                                    'platoId':10
                                                  } 
                                                }
                                              }),
                        400: openapi.Response('respuesta fallida',
                                              examples={
                                                'application/json':{
                                                  'message':'Error al crear la preparacion',
                                                  'content':'errores'
                                                }
                                              })})
@api_view(http_method_names=['POST'])
def crearPreparacion(request):
  serializador = PreparacionSerializer(data=request.data)

  if serializador.is_valid():
    serializador.save()
    return Response(data={
      'message':'Preparacion agregada exitosamente al plato',
      'content':serializador.data
    }, status=status.HTTP_201_CREATED)
  
  else:
    return Response(data={
      'message':'Error al crear la preparacion',
      'content': serializador.errors
    },status=status.HTTP_400_BAD_REQUEST)
  
@swagger_auto_schema(method='get', responses={200: openapi.Response(description='recetas', examples={
  'application/json': {
    'content': 'PlatoConIngredientesYPreparacionesModel'
  }
}, schema=PlatoConIngredientesYPreparacionesSerializer)})
@api_view(http_method_names=['GET'])
def buscarRecetas(request):
  print(request.query_params)
  # https://docs.djangoproject.com/en/5.0/topics/db/queries/#field-lookups
  if request.query_params.get('nombre'):
    # obtenemos el valor del query param
    nombre = request.query_params.get('nombre')

    # buscamos los platos por su filtro
    resultado = Plato.objects.filter(
      nombre__icontains=nombre).all() # .query
  
    serializador = PlatoConIngredientesYPreparacionesSerializer(
      instance=resultado, many=True)

    print(resultado)
    return Response(data={
      'content': serializador.data
    })
  else:
    return Response(data={
      'message':'Falta el nombre en el query param'
    }, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(http_method_names=['POST'])
def crearCheff(request):
  serializador = RegistroCheffSerializer(data=request.data)
  if serializador.is_valid():
    nuevo_cheff = Cheff(nombre = serializador.validated_data.get('nombre'), 
                        correo = serializador.validated_data.get('correo'))
    # set_password > sirve para generar el hash de nuestra password
    nuevo_cheff.set_password(serializador.validated_data.get('password'))
    nuevo_cheff.save()
    print(request.data.get('correo'))

    return Response(data={
      'message':'cheff creado exitosamente',
      'content': serializador.data
    }, status=status.HTTP_201_CREATED)
  else:
    return Response(data={
      'message':'Error al crear el cheff',
      'content': serializador.errors
    }, status=status.HTTP_400_BAD_REQUEST)