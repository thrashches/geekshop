from django.db import models
from django.conf import settings
from mainapp.models import Product

# Create your models here.


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="basket")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name="количество товара", default=0)
    add_datetime = models.DateTimeField(verbose_name="время добавления", auto_now_add=True)

    @property
    def product_price(self):
        pass

    @property
    def total_quantity(self):
        _items = Basket.objects.filter(user=self.user)
        _total = sum(list(map(lambda x: x.quantity, _items)))
        return _total


    @property
    def total_price(self):
        _items = Basket.objects.filter(user=self.user)
        _total = sum(list(map(lambda x: x.product.price * x.quantity, _items)))
        return _total
