from django.urls import path
from .views import *

urlpatterns = [
    path('brand/', BrandViewSet.as_view(), name='all_create_brand'),
    path('brand/<int:pk>/', BrandDetailView.as_view(),
         name='retrieve_update_delete_brand'),

    path('color/', ColorCreateView.as_view(), name='create_color'),
    path('color/<int:pk>/', ColorDetailView.as_view(),
         name='retrieve_update_delete_color'),

    path('material/', MaterialCreateView.as_view(),
         name='create_material'),
    path('material/<int:pk>/', MaterialDetailView.as_view(),
         name='retrieve_update_delete_material'),

    path('cloth_type/', ClothTypeCreateView.as_view(),
         name='create_cloth_type'),
    path('cloth_type/<int:pk>/', ClothTypeDetailView.as_view(),
         name='retrieve_update_delete_material'),

    path('product/', ProductListCreateView.as_view(),
         name='list_create_product'),
    path('product/<int:pk>/', ProductDetailView.as_view(),
         name='retrieve_update_delete_product_property'),
]
