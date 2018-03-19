# Generated by Django 2.0.2 on 2018-03-17 13:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=250)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('description', models.CharField(max_length=400)),
                ('text_recipe', models.TextField()),
                ('ingredients', models.TextField(default='')),
                ('img_main', models.ImageField(upload_to='photo/')),
                ('img1', models.ImageField(upload_to='photo/')),
                ('img2', models.ImageField(upload_to='photo/')),
                ('img3', models.ImageField(upload_to='photo/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food', models.CharField(max_length=35)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_food.Recipe'),
        ),
    ]
