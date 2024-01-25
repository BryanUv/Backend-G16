from sqlalchemy import Column, types, ForeignKey
from variables import conexion

class DireccionModel(conexion.Model):
  id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
  calle = Column(type_=types.Text)
  numero = Column(type_=types.String(20))
  referencia = Column(type_=types.Text)
  predeterminada = Column(type_=types.Boolean, 
                          default=False )# si queremos colocar un valor por defecto de crear
  # Relaciones
  usuarioId = Column(ForeignKey(column='usuarios.id'), nullable=False, name='usuario_id')

  __tablename__ = 'direcciones'