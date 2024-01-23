from rest_framework import serializers
from .models import *

class empresaSerializer(serializers.ModelSerializer):
  class Meta:
    model = empresa
    fields = '__all__'

class representanteSerializer(serializers.ModelSerializer):
  class Meta:
    model = representante
    fields = '__all__'

class empresaRepresentanteSerializer(serializers.ModelSerializer):
  class Meta:
    model = empresaRepresentante
    fields = '__all__'

class empresaRepresentanteReadSerializer(serializers.ModelSerializer):
  class Meta:
    model = empresaRepresentante
    exclude = []
    depth = 2