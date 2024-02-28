from rest_framework import serializers
from .models import Plato, Ingrediente, Preparacion, Cheff

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

class RegistroCheffSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cheff
    # fields = '__all__'
    exclude = ['groups','user_permissions','last_login']
    # https://www.django-rest-framework.org/api-guide/serializers/#additional-keyword-arguments
    # podemos indicar que atributos o columnas de la tabla son solo escritura o solo lectura
    extra_kwargs = {
      'password': {
        'write_only': True
      },
      'is_staff': {
        'read_only': True
      },
      'is_active': {
        'write_only': True
      }
    }