from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from fashion_store.apps.user.serializers import UserSLIOSerializer, \
    UserSerializer

UserModel = get_user_model()


class UserCreateView(CreateAPIView):
    """ Create new user """

    serializer_class = UserSLIOSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            data={"message": "Created successfully"},
            status=status.HTTP_201_CREATED)


class UserRetriveUpdateView(RetrieveUpdateDestroyAPIView):
    """ User profile """

    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    http_method_names = ['get', 'put', 'delete']

    def get_object(self):
        user = self.request.user

        if user:
            return self.request.user

        return Response(
            data={"message": "This user doesn't have profile"},
            status=status.HTTP_409_CONFLICT)

    def update(self, request, *args, **kwargs):
        email = self.request.data.get('email', None)
        password = self.request.data.get('password', None)
        print(request.data)
        if email or password:
            return Response(
                data={"message": "If you wont update email or password "
                                 "use another API endpoints"},
                status=status.HTTP_400_BAD_REQUEST)
        return super().update(self, request, *args, **kwargs)


@api_view(['PATCH', ])
def update_password(request):
    user = request.user

    user_instance = UserModel.objects.get(id=user.id)
    hashed_password = user_instance.password

    password = request.data.get('password', None)
    new_password = request.data.get('new_password', None)

    if not check_password(password, hashed_password):
        return Response(data={"message": "You write incorrect password"},
                        status=status.HTTP_400_BAD_REQUEST)

    user_instance.set_password(new_password)
    user_instance.save()

    return Response(data={"message": "Successfully update user password"},
                    status=status.HTTP_200_OK)
#
# @api_view(['PATCH', ])
# def update_email(request):
#     pass
