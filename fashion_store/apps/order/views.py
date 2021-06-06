from rest_framework import status
from rest_framework.generics import ListAPIView, GenericAPIView, CreateAPIView, \
    DestroyAPIView
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import *


class OrderView(ListAPIView):
    """ Endpoint that allows authenticated
    user to get list (history of buying) and get cart """

    serializer_class = OrderOutputStorySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user

        return OrderModel.objects.filter(user=user, hide=False).exclude(
            status='Opened')


class CartDetailView(DestroyModelMixin, UpdateModelMixin, GenericAPIView):
    """ Endpoints that allows owner R U D Order"""
    serializer_class = CartSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated(), ]
        else:
            return [IsAuthenticated(), ]  # HaveCartPermission

    # __________________________ get _______________________________________
    def get_cart_or_create(self, user=None):
        if user is None:
            user = self.request.user
        cart = OrderModel.objects.get_or_create(user=user, status='Opened')

        return cart[0]

    def get_cart_api(self):
        cart = self.get_cart_or_create()
        serialized_cart = CartSerializer(cart)
        return serialized_cart.data

    def check_order_preparation(self):
        return self.request.query_params.get('order_preparation') is not None

    @staticmethod
    def check_available_quantity(selected_p):
        id_ = selected_p['product_property_id']
        p_property = ProductPropertyModel.objects.get(id=id_)

        available = p_property.quantity
        necessary = selected_p['quantity']
        return available - necessary >= 0

    def get_order_preparation(self):
        cart = self.get_cart_or_create()
        order_preparation = {"available": {}, "out_of_stock": [],
                             "owners_id": []}

        q_selected_p = SelectedProductView.get_selected_product_by_order(cart)

        for selected_p in q_selected_p:
            owner = UserModel.objects.filter(
                ordermodel=selected_p["order_id"]).values('id', 'first_name',
                                                          'last_name')[0]

            if not self.check_available_quantity(selected_p):
                order_preparation["out_of_stock"].append(selected_p)
                continue

            if owner['id'] in order_preparation['owners_id']:
                order_preparation["available"][owner['id']]['products']. \
                    append(selected_p)
            else:
                order_preparation['owners_id'].append(owner['id'])

                data_ = {'owner': owner, 'products': [selected_p], 'price': 0}
                order_preparation["available"][owner['id']] = data_

        return order_preparation

    @staticmethod
    def add_total_price(data_):
        return data_

    def get_order_preparation_api(self):
        order_preparation = self.get_order_preparation()

        order_preparation = self.add_total_price(order_preparation)

        output_serializer = AvailableOrderSerializer(data=order_preparation)
        output_serializer.is_valid()
        return output_serializer.data

    #
    #     queryset = SelectedProductView.get_order_selected_product(order)
    #
    #     for selected_product in queryset:
    #         product_property = SelectedProductsModel.objects.filter(
    #             pk=selected_product.id).values()
    #
    #         data = {"id": selected_product.id,
    #                 "product_property": product_property,
    #                 "quantity": selected_product.quantity}
    #
    #         if not self.check_available_quantity(selected_product):
    #             output["out_of_stock"].append(data)
    #             continue
    #
    #         user_id = selected_product.order.user.id
    #
    #         if user_id in users_id:
    #             output["available"][user_id].append(data)
    #         else:
    #             users_id.append(user_id)
    #             output["available"][user_id] = [data]
    #
    #     output["available"] = self.rename_dict_key(output["available"])
    #

    # API method
    def get(self, request, **kwargs):

        if self.check_order_preparation():
            data = self.get_order_preparation_api()
        else:
            data = self.get_cart_api()

        return Response(data=data, status=status.HTTP_200_OK)

    # API method
    # def delete(self, request, *args, **kwargs):
    #     user = self.request.user
    #
    #     return super().destroy(request, *args, pk=cart_id)
    # def update_recipient(self):
    #     cart = self.get_object()
    #     recipient = self.request.data.get("recipient")
    #     cart.recipient = recipient
    #     cart.save()
    #
    # def update_status(self):
    #     cart = self.get_object()
    #     cart_status = self.request.data.get("status")
    #     cart.status = cart_status
    #     cart.save()
    #
    # def check_recipient(self):
    #     return self.request.data.get('recipient') is not None
    #
    # def check_available_actions(self):
    #     cart_status = self.request.data.get('status')
    #
    #     if cart_status is None:
    #         return None
    #     elif cart_status == 'Processed':
    #         if self.check_recipient():
    #             return ["status", "recipient"]
    #         else:
    #             return None
    #     return ["status"]
    #
    # def check_selected_product(self):
    #     return self.request.data.get("selected_product") is not None
    #
    # # API method
    # def patch(self, request, *args, **kwargs):
    #
    #     if self.check_selected_product():
    #         return Response(data={"message": "For updating selected_product"
    #                                          "use another endpoint"},
    #                         status=status.HTTP_400_BAD_REQUEST)
    #
    #     available_actions = self.check_available_actions()
    #
    #     if available_actions is None:
    #         return Response(data={"message": "Bad request"},
    #                         status=status.HTTP_400_BAD_REQUEST)
    #
    #     if "status" in available_actions:
    #         self.update_status()
    #
    #     if "recipient" in available_actions:
    #         self.update_recipient()
    #
    #     return Response(data={"message": "Successfully update"},
    #                     status=status.HTTP_205_RESET_CONTENT)


# def check_enough_quantity(product_property, quantity):
#     return product_property.quantity - quantity >= 0


class SelectedProductView(CreateAPIView):
    serializer_class = CreateSelectedProductSerializer
    permission_classes = (IsAuthenticated,)  # HaveCart

    @staticmethod
    def get_selected_product_by_order(order):
        return SelectedProductsModel.objects.filter(order=order).values(
            'id', 'product_property_id', 'order_id', 'quantity')

    def perform_create(self, serializer):
        user = self.request.user
        cart = CartDetailView.get_cart_or_create(..., user)
        serializer.save(order=cart)


class SelectedProductDetailView(DestroyAPIView):
    queryset = SelectedProductsModel
