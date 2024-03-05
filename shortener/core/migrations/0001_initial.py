# Generated by Django 5.0.3 on 2024-03-05 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlRedirect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destiny', models.URLField(max_length=512)),
                ('slug', models.SlugField(max_length=128, unique=True)),
                ('created_in', models.DateTimeField(auto_now_add=True)),
                ('updated_in', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
