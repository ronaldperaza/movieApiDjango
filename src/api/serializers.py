from django.db import models
from django.db.models import fields
from .models import Pelicula, PeliculaFavorita
from rest_framework import serializers

#serializar transformar a formato json 

class PeliculaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        #todos los campos del models pelicula
        fields = '__all__'

class PeliculaFavoritaSerializers(serializers.ModelSerializer):

    pelicula = PeliculaSerializers()

    class Meta:
        models = PeliculaFavorita
        fields = ['pelicula']