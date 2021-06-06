from django.urls import path

from .views import *

urlpatterns = [
    path('', OrderView.as_view(),
         name='list of user orders'),
    path('my_cart/', CartDetailView.as_view(),
         name='R(with selected products and recipient (if available)) U D'),

    path('selected_product/', SelectedProductView.as_view(),
         name='User add product property to order'),
    path('selected_product/<int:pk>/', SelectedProductDetailView.as_view(),
         name='D Selected product from order')

    # path('confirm_order/', OrderForProductOwnerView.as_view(),
    #       name='for order property owner list of order from user')
    # path('confirm_order/<int:pk>', OrderForProductOwnerDetailView.as_view(),
    #       name='confirm or cancel order')
]
