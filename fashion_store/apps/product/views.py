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
        Can create and """

    serializer_class = BrandSerializer
    queryset = BrandModel.objects.all()

    # def get_permissions(self):
    #     if self.request.method == 'POST':
    #         self.permission_classes = (IsAdminUser,)
    #     return super(BrandViewSet, self).get_permissions()


class BrandDetailView(RetrieveUpdateDestroyAPIView):
    """ Endpoint for create and list Brand """
    serializer_class = BrandSerializer
    queryset = BrandModel.objects.all()
    http_method_names = ['get', 'put', 'delete']

    def get_permissions(self):
        if self.request.method in ('PUT', 'DELETE'):
            self.permission_classes = (IsAdminUser,)
        return super(BrandDetailView, self).get_permissions()


class ColorCreateView(CreateAPIView):
    serializer_class = ColorSerializer
    queryset = ColorModel.objects.all()
    # permission_classes = (IsAdminUser,)


class ColorDetailView(UpdateAPIView, DestroyAPIView):
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

    def create(self, request, *args, **kwargs):
        product_properties = self.request.data.pop("product_properties", None)

        if product_properties is None:
            return Response(data={"message": ""},
                            status=status.HTTP_400_BAD_REQUEST)

        product = super(ProductListCreateView,
                        self).create(request, data=self.request.data)

        for product_property in product_properties:
            product_property["product"] = product.data["id"]

            obj_product_properties = CreateProductPropertySerializer(
                data=product_property)
            obj_product_properties.is_valid()
            obj_product_properties.save()

        return Response(data={"message": "Product successfully created"},
                        status=status.HTTP_201_CREATED)


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CreateProductSerializer
    queryset = ProductModel.objects.all()

    # permission_classes = (IsOwner,)

    def update(self, request, *args, **kwargs):
        properties = self.request.data.pop('product_properties', None)
        product_id = kwargs["pk"]

        super().update(request, *args, **kwargs)

        if not properties:
            return Response(data={"message": "Product successfully update"},
                            status=status.HTTP_205_RESET_CONTENT)

        old_data = list(ProductPropertyModel.objects.filter(
            product_id=product_id).values_list("id", flat=True))

        # update all available and create new
        for product_property in properties:
            property_id = product_property.get("id", None)
            product_property["product"] = product_id

            # update
            if property_id in old_data:
                ProductPropertyModel.objects.filter(id=property_id).update(
                    **product_property)

            # create
            else:
                instance = CreateProductPropertySerializer(
                    data=product_property)
                instance.is_valid()
                instance.save()

        # delete
        new_list_id = [x["id"] for x in properties if x.get("id", None)]
        for old_data_id in old_data:
            if old_data_id not in new_list_id:
                ProductPropertyModel.objects.filter(id=old_data_id).delete()

        return Response(data={"message": "Product and product property "
                                         "successfully update"},
                        status=status.HTTP_205_RESET_CONTENT)
