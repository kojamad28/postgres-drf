import uuid

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):

    def create_user(self, username, email, password=None):

        if not username:
            raise ValueError("Users must have a username.")

        user = self.model(
            username=username,
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username=username,
            email=self.normalize_email(email),
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False
    )
    username = models.CharField(
        verbose_name=_("username"),
        max_length=20,
        unique=True
    )
    email = models.EmailField(
        verbose_name=_("email address"),
        max_length=254,
        blank=True
    )
    is_active = models.BooleanField(
        verbose_name=_("active"),
        default=True
    )
    is_staff = models.BooleanField(
        verbose_name=_("admin"),
        default=False
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username
