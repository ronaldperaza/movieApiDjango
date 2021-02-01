# Generated by Django 3.0.4 on 2021-01-31 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('estreno', models.IntegerField(default=2000)),
                ('imagen', models.URLField(help_text='Imagen traida de img')),
                ('resumen', models.TextField(help_text='movie description')),
            ],
            options={
                'ordering': ['titulo'],
            },
        ),
    ]