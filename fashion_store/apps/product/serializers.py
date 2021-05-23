from rest_framework.serializers import ModelSerializer
from .models import *
from fashion_store.apps.user.serializers import UserProductSerializer


class BrandSerializer(ModelSerializer):
    """ Serializer for create and output Brand """

    class Meta:
        model = BrandModel
        exclude = ['created', 'updated']


class ColorSerializer(ModelSerializer):
    """ Serializer for create and output Color """

    class Meta:
        model = ColorModel
        exclude = ['created', 'updated']


class MaterialSerializer(ModelSerializer):
    """ Serializer for create and output Material """

    class Meta:
        model = MaterialModel
        exclude = ['created', 'updated']


class ClothTypeSerializer(ModelSerializer):
    """ Serializer for create and output Cloth Type """

    class Meta:
        model = ClothTypeModel
        exclude = ['created', 'updated']


class ProductPropertySerializer(ModelSerializer):
    """ Serializer for output Product Property
        Used with ProductSerializer and CreateProductSerializer """

    class Meta:
        model = ProductPropertyModel
        exclude = ['created', 'updated', 'product']
        depth = 1


class CreateProductPropertySerializer(ModelSerializer):
    """ Serializer for create Product Property
        Used with view ProductListCreateView """

    class Meta:
        model = ProductPropertyModel
        exclude = ['created', 'updated']


# class UpdateProductPropertySerializer(ModelSerializer):
#     """ Serializer for update Product Property
#         Used with view ProductDetailView """
#
#     class Meta:
#         model = ProductPropertyModel
#         exclude = ['created', 'updated',]


class ProductSerializer(ModelSerializer):
    """ Serializer for output Product with Product Property """
    owner = UserProductSerializer()
    cloth_type = ClothTypeSerializer()
    material = MaterialSerializer()
    brand = BrandSerializer()
    product_property = ProductPropertySerializer(many=True)

    class Meta:
        model = ProductModel
        fields = ['id', 'name', 'description', 'brand', 'cloth_type',
                  'owner', 'material', 'product_property']
        depth = 1


class CreateProductSerializer(ModelSerializer):
    """ Serializer fot create product  with Product Property """
    product_properties = ProductPropertySerializer

    class Meta:
        model = ProductModel
        exclude = ('created', 'updated', 'owner')

    # def update(self, instance, validated_data):
    #     product_properties = validated_data.pop('product_properties', None)
    #
    #     product = ProductModel.objects.filter(pk=instance.pk).update(
    #         **validated_data)
    #     if not product_properties:
    #         return instance
    #
    #     list_properties = ProductPropertyModel.objects.filter(
    #         product__id=product.id).values_list()
    #     print(list_properties)
