# Generated by Django 2.0.2 on 2018-03-09 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_food', '0002_auto_20180309_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(default=''),
        ),
    ]