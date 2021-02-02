# from django.shortcuts import render

from .models import Pelicula, PeliculaFavorita
from .serializers import PeliculaSerializers, PeliculaFavoritaSerializers

from django.shortcuts import get_object_or_404

from rest_framework import serializers, viewsets, views, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializers

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['titulo', 'estreno']
    ordering_fields = ['favoritos']


class MarcarPeliculaFavorita(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

  # POST -> Se usa para crear un recurso sin un identificador
  # PUT -> Se usa para crear/reemplazar un recurso con un identificador

    def post(self, request):
        pelicula = get_object_or_404 ( 
            Pelicula, id = self.request.data.get('id', 0) 
        )

        favorita, created = PeliculaFavorita.objects.get_or_create (
            pelicula = pelicula, usuario = request.user
        )

        # por defecto suponemos que se crea bien
        content = { 'id': pelicula.id, 'favorita': True } 

        # Si no se ha creado es que ya existe, entonces borramos el favorito
        if not created:
            favorita.delete()
            content['favorita'] = False

        return Response(content)



class ListarPeliculasFavoritas(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

# get -. se usa para hacer lecturas

    def get(self, request):
        peliculas_favoritas = PeliculaFavorita.objects.filter(
            usuario = request.user
        )
        serializer = PeliculaFavoritaSerializers(
            peliculas_favoritas, many = True
        )

        return Response(serializer.data)
