# Generated by Django 3.2.3 on 2021-05-24 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_productmodel_owner'),
        ('order', '0003_ordermodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selectedproductsmodel',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='selected_product', to='order.ordermodel', verbose_name='Order'),
        ),
        migrations.AlterField(
            model_name='selectedproductsmodel',
            name='product_property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_property', to='product.productpropertymodel', verbose_name='product_property'),
        ),
    ]