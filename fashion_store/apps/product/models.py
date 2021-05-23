from django.db import models
from utils.abstract_models import CreateUpdateModel
from django.contrib.auth import get_user_model
from colorfield.fields import ColorField

UserModel = get_user_model()


class ColorModel(CreateUpdateModel):
    name = models.CharField(max_length=20, verbose_name="Name")
    hex = ColorField(format='hexa')
    description = models.TextField(verbose_name="Description")

    class Meta:
        db_table = 'color'
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'
        ordering = ('name',)

    def str(self):
        return f'{self.name}'


class MaterialModel(CreateUpdateModel):
    name = models.CharField(max_length=20, unique=True,
                            verbose_name='Name')
    description = models.TextField(verbose_name="Description")

    class Meta:
        db_table = 'material'
        verbose_name = 'Material'
        verbose_name_plural = 'Materials'
        ordering = ('name',)

    def str(self):
        return f'{self.name}'


class ClothTypeModel(CreateUpdateModel):
    name = models.CharField(max_length=20, unique=True,
                            verbose_name='Name')
    description = models.TextField(verbose_name="Description")

    class Meta:
        db_table = 'cloth_type'
        verbose_name = 'ClothType'
        verbose_name_plural = 'ClothTypes'
        ordering = ('name',)

    def str(self):
        return f'{self.name}'


class BrandModel(CreateUpdateModel):
    name = models.CharField(max_length=50, verbose_name='Name')
    description = models.TextField(verbose_name="Description")

    class Meta:
        db_table = 'brand'
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
        ordering = ('name',)

    def __str__(self):
        return self.name


class ProductModel(CreateUpdateModel):
    man = 'Man'
    woman = 'Woman'
    kids = 'Kids'

    gender_choices = [
        (man, 'Man'),
        (woman, 'Woman'),
        (kids, 'Kids')
    ]

    name = models.CharField(max_length=20, verbose_name="Name")
    description = models.TextField(verbose_name="Description")
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE)
    gender = models.CharField(max_length=5, choices=gender_choices,
                              verbose_name='Gender')
    cloth_type = models.ForeignKey(ClothTypeModel, on_delete=models.CASCADE)
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    material = models.ForeignKey(MaterialModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('name',)

    def __str__(self):
        return self.name


class ProductPropertyModel(CreateUpdateModel):
    s = 'S'
    m = 'M'
    l = 'L'
    xl = 'XL'
    xxl = 'XXL'

    size_choices = [
        (s, 'S'),
        (m, 'M'),
        (l, 'L'),
        (xl, 'XL'),
        (xxl, 'XXL')
    ]

    size = models.CharField(max_length=4, choices=size_choices,
                            verbose_name='Size')
    quantity = models.PositiveIntegerField(verbose_name="Quantity")
    price = models.PositiveIntegerField(verbose_name="Price")
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE,
                                related_name="product_property")
    color = models.ForeignKey(ColorModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_property'
        verbose_name = 'ProductProperty'
        verbose_name_plural = 'ProductProperties'
