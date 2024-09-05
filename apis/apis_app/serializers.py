# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import apimodels

# Create a model serializer
class apiSerializer(serializers.HyperlinkedModelSerializer):
	# specify model and fields
	class Meta:
		model = apimodels
		fields = ('title', 'description')
