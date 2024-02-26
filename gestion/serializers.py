from rest_framework import serializers
from .models import Plato, Ingrediente, Preparacion

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

class IngredienteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Ingrediente
    fields = '__all__'

class PreparacionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Preparacion
    fields = '__all__'

class PlatoConIngredientesYPreparacionesSerializer(serializers.ModelSerializer):
  ingredientes = IngredienteSerializer(many=True)
  # Si queremos definir un atributo que no existe en nuestro modelo pero queremos utilizar un atributo como referencia entonces,
  # tenemos que definir el parametro source
  pasos = PreparacionSerializer(many=True, source='preparaciones')
  class Meta:
    model = Plato
    fields = '__all__'