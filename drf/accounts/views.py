from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import CustomUser
from .serializers import UserListSerializer, UserDetailSerializer


class UserListView(ListAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = UserListSerializer


class UserDetailView(RetrieveAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = "username"
