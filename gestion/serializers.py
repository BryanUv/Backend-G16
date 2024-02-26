from rest_framework import serializers
from .models import Plato

class PlatoSerializer(serializers.ModelSerializer):
  class Meta:
    # el modelo en el cual se utilizara la referencia para convertir la data de bd y viceversa
    model = Plato
    # fields > indicar que columna quiero mostrar
    # exclude > indicar columnas que quiero excluir
    #  NOTA: solo se puede usar uno de los dos, no los dos al mismo tiempo pq dara errores
    # fields = ['id','nombre','foto']
    # si estoy utilizando todos los atributos del modulo
    fields = '__all__'

    # exclude = ['id']