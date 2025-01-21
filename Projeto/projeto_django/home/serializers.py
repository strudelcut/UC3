from rest_framework import serializers
from .models import Imagem


class SerializarImagem(serializers.ModelSerializer):

    class Meta:
        model = Imagem
        fields = '__all__'