# Generated by Django 4.1.5 on 2023-01-31 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=3000, null=True, verbose_name='Mahsulot haqida'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.CharField(max_length=200, null=True, verbose_name='Rasm file_id'),
        ),
        migrations.AlterField(
            model_name='product',
            name='productname',
            field=models.CharField(max_length=50, verbose_name='Mahsulot nomi'),
        ),
    ]