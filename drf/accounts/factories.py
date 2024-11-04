from factory import LazyAttribute
from factory.django import DjangoModelFactory

from .models import CustomUser


class UserFactory(DjangoModelFactory):

    username = "user"
    email = LazyAttribute(lambda u: f"{u.username}@example.com")
    password = "password"
    is_active = True
    is_admin = False

    class Meta:
        model = CustomUser
        django_get_or_create = ("username",)
