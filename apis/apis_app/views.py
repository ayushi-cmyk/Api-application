from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

# import local data
from .serializers import apiSerializer
from .models import apimodels



class apisViewSet(viewsets.ModelViewSet):

	queryset = apimodels.objects.all()

	serializer_class = apiSerializer
