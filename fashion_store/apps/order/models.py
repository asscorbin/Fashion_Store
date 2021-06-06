from django.contrib.auth import get_user_model
from fashion_store.apps.product.models import ColorModel, ProductPropertyModel
from utils.abstract_models import CreateUpdateModel
from django.db import models
from phone_field import PhoneField

UserModel = get_user_model()


class RecipientModel(CreateUpdateModel):
    email = models.EmailField(max_length=100, verbose_name='Email')
    first_name = models.CharField(max_length=20, verbose_name='Name')
    last_name = models.CharField(max_length=20, verbose_name='Last Name')
    city = models.CharField(max_length=100, verbose_name='City',
                            default='')
    state = models.CharField(max_length=100, verbose_name='State', default='')
    zip = models.CharField(max_length=100, verbose_name='ZIP', default='')
    phone = PhoneField(blank=True, verbose_name='Contact phone number')
    street = models.CharField(max_length=30, verbose_name="street")

    class Meta:
        db_table = 'recipient'
        verbose_name = 'Recipient'
        verbose_name_plural = 'Recipients'

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class OrderModel(CreateUpdateModel):
    status_dict = (
        ("Completed", 'Completed'),
        ("Opened", 'Opened'),
        ("Processed", 'Processed'),
        ("Canceled", 'Canceled'))

    status = models.CharField(max_length=10, choices=status_dict,
                              verbose_name="status", default='Opened')
    hide = models.BooleanField(verbose_name="Hide", default=False)

    recipient = models.OneToOneField(RecipientModel, on_delete=models.CASCADE,
                                     null=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'order'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.user


class SelectedProductsModel(CreateUpdateModel):
    order = models.ForeignKey(OrderModel, verbose_name='Order',
                              related_name='selected_product',
                              on_delete=models.SET_NULL, null=True)

    product_property = models.ForeignKey(ProductPropertyModel,
                                         verbose_name='product_property',
                                         related_name='product_property',
                                         on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(verbose_name="Quantity")

    class Meta:
        db_table = 'selected_product'
        verbose_name = 'SelectedProduct'
        verbose_name_plural = 'SelectedProducts'

    def __str__(self):
        return self.order
