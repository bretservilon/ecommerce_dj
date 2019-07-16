# Generated by Django 2.2.2 on 2019-06-16 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
