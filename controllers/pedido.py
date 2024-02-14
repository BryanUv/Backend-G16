from flask_restful import Resource, request
from models import Pedido, DetallePedido, Trago
from flask_jwt_extended import get_jwt_identity, jwt_required, get_jwt
from decoradores import validar_invitado, validar_barman
from dtos import CrearPedidoDTO, ListarPedidosDTO
from variables import conexion

class PedidosController(Resource):

  # cuando queremos que un controlador requiera una manera obligatoria una token
  # @jwt_required()
  @validar_invitado
  def post(self):
    # para acceder al identity configurado en la creacion de la token
    identity = get_jwt_identity()
    # devolvera la payload de la token y dentro de ella todas sus propiedades como el identity, exp entre
    # otros
    # get_jwt()
    dto = CrearPedidoDTO()
    try:
      data_validada = dto.load(request.get_json())
      print(data_validada)
      # Empezar una transaccion
      # Primero creo el nuevo pedido
      with conexion.session.begin() as transaccion:
        nuevo_pedido = Pedido(invitado = identity)
        conexion.session.add(nuevo_pedido)

        for detalle in data_validada.get('detalle'):
          trago_existente = conexion.session.query(Trago).filter_by(
            id=detalle.get('tragoId')).first()
          
          if not trago_existente:
            raise Exception('El trago no existe')

          nuevo_detalle_pedido = DetallePedido(cantidad=detalle.get('cantidad'),
                                              trago=detalle.get('tragoId'), pedido=nuevo_pedido.id)
          conexion.session.add(nuevo_detalle_pedido)

        transaccion.commit()
      return {
        'message':''
      }
    
    except Exception as e:
      # si alguna operacion de la transaccion falla entonces todo queda descartado
      conexion.session.rollback()
      return {
        'message':'Error al crear el pedido',
        'content':e.args
      },400
    
  @validar_barman
  def get(self):
    """
    file: controllers/devolverPedidos.yml
    """
    # devolver los pedidos PERO SOLAMENTE LO PUEDEN V ER LOS BARMANS
    # Crear un DTO para transformar la data al momento de enviarla
    pedidos = conexion.session.query(Pedido).all()
    print(pedidos[0].detallePedidos)
    dto = ListarPedidosDTO()
    # many -> indicar que estamos pasando una lista de instancias por lo que tendra que iterar y transformar
    # cada una de ellas
    resultado = dto.dump(pedidos, many=True)

    return {
      'content': resultado
    },200