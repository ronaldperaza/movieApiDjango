# Generated by Django 3.0.4 on 2021-02-02 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_peliculafavorita'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='favoritos',
            field=models.IntegerField(default=0),
        ),
    ]
