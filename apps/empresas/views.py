from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *

# Create your views here.
class empresaViewSet(viewsets.ModelViewSet):

  queryset = empresa.objects.all()
  serializer_class = empresaSerializer
  permission_classes = [permissions.IsAuthenticated]

class representanteViewSet(viewsets.ModelViewSet):

  queryset = representante.objects.all()
  serializer_class = representanteSerializer
  # permission_classes = [permissions.IsAuthenticated]

class relacionViewSet(viewsets.ModelViewSet):

  queryset = empresaRepresentante.objects.all()
  serializer_class = empresaRepresentanteReadSerializer
  # permission_classes = [permissions.IsAuthenticated]

  def get_serializer_class(self):
    if self.action in ["list", "retrieve"]:
      return empresaRepresentanteReadSerializer
    return empresaRepresentanteSerializer
    