from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Pelicula(models.Model):
    titulo = models.CharField(max_length = 150)
    estreno = models.IntegerField(default = 2000)
    imagen = models.URLField(help_text = "Imagen traida de img")
    resumen = models.TextField(help_text = "movie description")
    favoritos = models.IntegerField(default = 0)

    class Meta:
        ordering = ['titulo']


class PeliculaFavorita(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete = models.CASCADE)
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)


from django.db.models.signals import post_save, post_delete

def update_favoritos(sender, instance, **kwars):
    count = instance.pelicula.peliculafavorita_set.all().count()
    instance.pelicula.favoritos = count
    instance.pelicula.save()

# n el post delete se pasa la copia de la instancia que ya no existe
post_save.connect(update_favoritos, sender = PeliculaFavorita)
post_delete.connect(update_favoritos, sender = PeliculaFavorita)