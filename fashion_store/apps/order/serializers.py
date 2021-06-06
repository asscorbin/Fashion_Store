from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *
from ..product.serializers import ProductPropertyForOutputHistorySerializer


class OrderOutputStoryProductPropertySerializer(ModelSerializer):
    """ Output history of user buying, work with OrderView """

    # product_property = ProductPropertyForOutputHistorySerializer()

    class Meta:
        model = SelectedProductsModel
        fields = ('quantity', 'product_property')


class OrderOutputStorySerializer(ModelSerializer):
    """ Output history of user buying, work with OrderView """
    selected_product = OrderOutputStoryProductPropertySerializer(many=True)

    class Meta:
        model = OrderModel
        fields = ('id', 'status', 'recipient', 'updated', 'selected_product')
        depth = 1


class SelectedProductSerializer(ModelSerializer):
    """ Selected Product for CartSerializer """
    product_property = ProductPropertyForOutputHistorySerializer()
    price = models.PositiveIntegerField(verbose_name="price")

    class Meta:
        model = SelectedProductsModel
        fields = ('id', 'product_property', 'quantity')


class CartSerializer(ModelSerializer):
    """ Work with CartDetailView """
    selected_product = SelectedProductSerializer(many=True, required=False)

    class Meta:
        model = OrderModel
        fields = ('selected_product',)


class CreateSelectedProductSerializer(ModelSerializer):
    """ Use for creating Selected Product, work with SelectedProductView """

    class Meta:
        model = SelectedProductsModel
        fields = ('order', 'product_property', 'quantity')


class AvailableOrderSerializer(serializers.Serializer):
    available = serializers.DictField()
    out_of_stock = SelectedProductSerializer(many=True)

# class RecipientSerializer(ModelSerializer):
#     class Meta:
#         model = RecipientModel
#         fields = ['first_name', 'last_name', 'email', 'city', 'state',
#                   'street', 'phone', 'zip']


# class SelectedProductSerializer(ModelSerializer):
#     # product_property = ProductPropertySerializer(many=False)
#
#     class Meta:
#         model = SelectedProductsModel
#         fields = '__all__'


# class OrderSerializer(ModelSerializer):
#     # selected_product = SelectedProductSerializer(many=True, required=False)
#     # recipient = RecipientSerializer(many=False, required=False)
#
#     class Meta:
#         model = OrderModel
#         fields = ['id', 'recipient', 'status', 'updated']
#         # 'selected_product']
