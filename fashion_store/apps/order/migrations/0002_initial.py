# Generated by Django 3.2.3 on 2021-05-16 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='selectedproductsmodel',
            name='color',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='product.colormodel', verbose_name='Color'),
        ),
        migrations.AddField(
            model_name='selectedproductsmodel',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.ordermodel', verbose_name='Order'),
        ),
        migrations.AddField(
            model_name='selectedproductsmodel',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productmodel', verbose_name='Product'),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='recipient',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='order.recipientmodel'),
        ),
    ]
