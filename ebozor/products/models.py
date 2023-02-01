from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(verbose_name="Ism", max_length=100)
    username = models.CharField(verbose_name="Telegram username", max_length=100, null=True)
    telegram_id = models.BigIntegerField(verbose_name='Telegram ID', unique=True, default=1)
    email = models.CharField(verbose_name='Email', max_length=50, null=True)

    def __str__(self):
        return f"{self.id} - {self.telegram_id} - {self.full_name}"

class Product(models.Model):
    fan = [
        ('maruza', "Ma'ruza"),
        ('amaliy', "Amaliy"),
        ('labaratoriya', "Labaratoriya"),

    ]

    category_code = models.CharField(verbose_name="Fan kodi", max_length=20)
    category_name = models.CharField(verbose_name="Fan nomi", max_length=300)
    subcategory_code = models.CharField(verbose_name="Ma'ruza yoki amaliy kodi", max_length=20, choices=fan)
    subcategory_name = models.CharField(verbose_name="Ma'ruza yoki amaliy nomi", max_length=300, choices=fan)

    id = models.AutoField(primary_key=True)
    productname = models.CharField(verbose_name="Mavzu nomi", max_length=50)
    # photo = models.CharField(verbose_name="Rasm file_id", max_length=200, null=True, blank=True)
    # price = models.DecimalField(verbose_name="Narx", decimal_places=2, max_digits=8, null=True, blank=True)
    description = models.TextField(verbose_name="Maruza yoki amaliy haqida batafsil", max_length=3000, null=True)
    # photo = models.FilePathField(verbose_name="Fayl yuklang")
    # photo = models.FileField(verbose_name="Fayl yuklang")

    def __str__(self):
        return f"' {self.category_name} ' fani ' {self.subcategory_name} ' bo'limi ' {self.productname} ' mavzusi"