from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(verbose_name="имя", max_length=64, unique=True)
    description = models.TextField(verbose_name="описание", blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="имя продукта", max_length=128)
    image = models.ImageField(upload_to="products_images", blank=True)
    short_desc = models.CharField(verbose_name="краткое описание продукта", max_length=60, blank=True)
    description = models.TextField(verbose_name="описание продукта", blank=True)
    price = models.DecimalField(verbose_name="цена продукта", max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name="количество на складе", default=0)

    def __str__(self):
        return self.name


class Locations(models.Model):
    name = models.CharField(verbose_name="название места", max_length=128)
    city = models.CharField(verbose_name="город", max_length=60)
    phone = models.CharField(verbose_name="телефон", max_length=16)
    email = models.EmailField(verbose_name="email")
    address = models.CharField(verbose_name="адрес", max_length=300)

    def __str__(self):
        return self.name