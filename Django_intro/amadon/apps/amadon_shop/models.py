from __future__ import unicode_literals
from django.db import models


class Item(models.Model):
    item_name = models.CharField(max_length=255)
    item_price = models.DecimalField(max_digits=6, decimal_places=2)
    item_keycode = models.IntegerField(default=0)
    item_count = models.IntegerField(default=0)


class ShoppingCart(models.Model):
    quantity = models.IntegerField()
    items = models.ManyToManyField(Item, related_name='buyers')