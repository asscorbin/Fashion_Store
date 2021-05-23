from rest_framework.serializers import ModelSerializer

from .models import UserModel


class UserSLIOSerializer(ModelSerializer):
    """ Serializer for creating user """

    class Meta:
        model = UserModel

        fields = ['first_name', 'last_name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validation_data):
        user = UserModel.objects.create_user(**validation_data)
        return user


class UserSerializer(ModelSerializer):
    """ Serializer for output user profile """

    class Meta:
        model = UserModel
        fields = ['last_name', 'first_name', 'phone', 'city', 'state', 'zip']


class UserProductSerializer(ModelSerializer):
    """ Serializer for output like serializer method fields with product """

    class Meta:
        model = UserModel
        fields = ['first_name', 'phone', 'city']
