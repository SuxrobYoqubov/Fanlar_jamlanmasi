# Generated by Django 4.1.5 on 2023-02-01 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_description_alter_product_photo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AlterField(
            model_name='product',
            name='category_code',
            field=models.CharField(max_length=20, verbose_name='Fan kodi'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category_name',
            field=models.CharField(max_length=300, verbose_name='Fan nomi'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=3000, null=True, verbose_name='Maruza yoki amaliy haqida batafsil'),
        ),
        migrations.AlterField(
            model_name='product',
            name='productname',
            field=models.CharField(max_length=50, verbose_name='Mavzu nomi'),
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategory_code',
            field=models.CharField(choices=[('maruza', "Ma'ruza"), ('amaliy', 'Amaliy'), ('labaratoriya', 'Labaratoriya')], max_length=20, verbose_name="Ma'ruza yoki amaliy kodi"),
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategory_name',
            field=models.CharField(choices=[('maruza', "Ma'ruza"), ('amaliy', 'Amaliy'), ('labaratoriya', 'Labaratoriya')], max_length=300, verbose_name="Ma'ruza yoki amaliy nomi"),
        ),
    ]