# Generated by Django 2.1.1 on 2018-09-05 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Artiste',
        ),
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name="nom de l'artiste"),
        ),
    ]
