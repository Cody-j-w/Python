# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-16 21:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amadon_shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productkey',
            name='item',
        ),
        migrations.AddField(
            model_name='item',
            name='item_keycode',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='items',
            field=models.ManyToManyField(related_name='buyers', to='amadon_shop.Item'),
        ),
        migrations.DeleteModel(
            name='ProductKey',
        ),
    ]
