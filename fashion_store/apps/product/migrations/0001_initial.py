# Generated by Django 3.2.3 on 2021-05-16 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrandModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
                'db_table': 'brand',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ClothTypeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'ClothType',
                'verbose_name_plural': 'ClothTypes',
                'db_table': 'cloth_type',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ColorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('hex', models.CharField(max_length=7, verbose_name='Hex')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Color',
                'verbose_name_plural': 'Colors',
                'db_table': 'color',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='MaterialModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Material',
                'verbose_name_plural': 'Materials',
                'db_table': 'material',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.brandmodel')),
                ('cloth_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.clothtypemodel')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'product',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ProductPropertyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now=True, db_index=True)),
                ('size', models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XLL', 'XLL')], max_length=4, verbose_name='Size')),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
                ('price', models.PositiveIntegerField(verbose_name='Price')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.colormodel')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.materialmodel')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productmodel')),
            ],
            options={
                'verbose_name': 'ProductProperty',
                'verbose_name_plural': 'ProductProperties',
                'db_table': 'product_property',
            },
        ),
    ]