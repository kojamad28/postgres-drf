from rest_framework.serializers import ModelSerializer
from .models import CustomUser


class UserListSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ("username",)


class UserDetailSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        exclude = ("id", "is_active", "is_admin")
