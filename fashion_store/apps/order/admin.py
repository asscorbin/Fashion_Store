from django.contrib import admin
from .models import *

admin.site.register(RecipientModel)
admin.site.register(OrderModel)
admin.site.register(SelectedProductsModel)
