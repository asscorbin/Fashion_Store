from rest_framework import status
from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView, CreateAPIView, UpdateAPIView, \
    DestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .serializers import *
from .models import *


class BrandViewSet(ListCreateAPIView):
    """ Endpoint for create and list Brand
        Can create only admin """

    serializer_class = BrandSerializer
    queryset = BrandModel.objects.all()

    # def get_permissions(self):
    #     if self.request.method == 'POST':
    #         self.permission_classes = (IsAdminUser,)
    #     return super(BrandViewSet, self).get_permissions()


class BrandDetailView(RetrieveUpdateDestroyAPIView):
    """ Endpoint for R U D Brand
        Can U D only admin """
    serializer_class = BrandSerializer
    queryset = BrandModel.objects.all()
    http_method_names = ('get', 'put', 'delete')

    def get_permissions(self):
        if self.request.method in ('PUT', 'DELETE'):
            self.permission_classes = (IsAdminUser,)
        return super(BrandDetailView, self).get_permissions()


class ColorCreateView(CreateAPIView):
    """ Endpoint for C and list Color
        Can C only admin """
    serializer_class = ColorSerializer
    queryset = ColorModel.objects.all()
    # permission_classes = (IsAdminUser,)


class ColorDetailView(UpdateAPIView, DestroyAPIView):
    """ Endpoint for U D Brand
        Only for admin """
    serializer_class = ColorSerializer
    queryset = ColorModel.objects.all()
    http_method_names = ('put', 'delete')
    permission_classes = (IsAdminUser,)


class MaterialCreateView(CreateAPIView):
    serializer_class = MaterialSerializer
    queryset = MaterialModel.objects.all()
    # permission_classes = (IsAdminUser, )


class MaterialDetailView(UpdateAPIView, DestroyAPIView):
    serializer_class = MaterialSerializer
    queryset = MaterialModel.objects.all()
    http_method_names = ('put', 'delete')
    permission_classes = (IsAdminUser,)


class ClothTypeCreateView(CreateAPIView):
    serializer_class = ClothTypeSerializer
    queryset = ClothTypeModel.objects.all()
    # permission_classes = (IsAdminUser, )


class ClothTypeDetailView(UpdateAPIView, DestroyAPIView):
    serializer_class = ClothTypeSerializer
    queryset = ClothTypeModel.objects.all()
    http_method_names = ('put', 'delete')
    permission_classes = (IsAdminUser,)


class ProductListCreateView(ListCreateAPIView):
    queryset = ProductModel.objects.all()

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = (IsAuthenticated,)
        return super(ProductListCreateView, self).get_permissions()

    def perform_create(self, serializer):
        serializer.save(
            owner=self.request.user
        )

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductSerializer
        else:
            return CreateProductSerializer

    @staticmethod
    def create_property(property_data):
        instance = CreateProductPropertySerializer(data=property_data)
        instance.is_valid()
        instance.save()

    def create(self, request, *args, **kwargs):
        product_properties = self.request.data.pop("product_properties", None)

        if product_properties is None:
            return Response(data={"message": ""},
                            status=status.HTTP_400_BAD_REQUEST)

        product = super(ProductListCreateView,
                        self).create(request, data=self.request.data)

        for product_property in product_properties:
            product_property["product"] = product.data["id"]
            self.create_property(product_property)

        return Response(data={"message": "Product successfully created"},
                        status=status.HTTP_201_CREATED)


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    """ Endpoint that allows owner to edit product and property """
    serializer_class = CreateProductSerializer
    queryset = ProductModel.objects.all()

    # permission_classes = (IsOwner,)

    @staticmethod
    def update_property(prod_id, new_property):
        old_data = list(ProductPropertyModel.objects.filter(
            product_id=prod_id).values_list("id", flat=True))

        for obj_property in new_property:
            property_id = obj_property.get("id")
            obj_property["product"] = prod_id

            if property_id in old_data:
                ProductPropertyModel.objects.filter(id=property_id).update(
                    **obj_property)
            else:
                ProductListCreateView.create_property(obj_property)

    @staticmethod
    def delete_property(delete_property):
        for property_id in delete_property:
            ProductPropertyModel.objects.filter(id=property_id).delete()

    def update(self, request, *args, **kwargs):
        prod_id = kwargs["pk"]
        super().update(request, *args, **kwargs)

        new_property = self.request.data.pop('product_properties', None)
        if new_property:
            self.update_property(prod_id, new_property)

        delete_property = self.request.data.pop('delete_property', None)
        if delete_property:
            self.delete_property(delete_property)

        return Response(data={"message": "successfully update"},
                        status=status.HTTP_205_RESET_CONTENT)
