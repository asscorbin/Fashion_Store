# Generated by Django 3.2.3 on 2021-05-16 06:40

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now=True, db_index=True)),
                ('status', models.CharField(choices=[('Completed', 'Completed'), ('Opened', 'Opened'), ('Processed', 'Processed'), ('Canceled', 'Canceled')], max_length=10, verbose_name='status')),
                ('hide', models.BooleanField(verbose_name='Hide')),
            ],
            options={
                'verbose_name': 'Recipient',
                'verbose_name_plural': 'Recipients',
                'db_table': 'recipient',
            },
        ),
        migrations.CreateModel(
            name='RecipientModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now=True, db_index=True)),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('first_name', models.CharField(max_length=20, verbose_name='Name')),
                ('last_name', models.CharField(max_length=20, verbose_name='Last Name')),
                ('city', models.CharField(default='', max_length=100, verbose_name='City')),
                ('state', models.CharField(default='', max_length=100, verbose_name='State')),
                ('zip', models.CharField(default='', max_length=100, verbose_name='ZIP')),
                ('phone', phone_field.models.PhoneField(blank=True, max_length=31, verbose_name='Contact phone number')),
                ('street', models.CharField(max_length=30, verbose_name='street')),
            ],
            options={
                'verbose_name': 'Recipient',
                'verbose_name_plural': 'Recipients',
                'db_table': 'recipient_table',
            },
        ),
        migrations.CreateModel(
            name='SelectedProductsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now=True, db_index=True)),
                ('size', models.CharField(max_length=3)),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
            ],
            options={
                'verbose_name': 'SelectedProduct',
                'verbose_name_plural': 'SelectedProducts',
                'db_table': 'selected_product',
            },
        ),
    ]
