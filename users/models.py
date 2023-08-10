from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from users.managers import GeekUserManager
from django.utils import timezone


class GeekUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("Email адрес", unique=True)
    is_staff = models.BooleanField("Статус персонала", default=False)
    is_active = models.BooleanField("Активный", default=True)
    date_joined = models.DateTimeField("Дата регистрации", default=timezone.now)
    first_name = models.CharField("Имя", max_length=50, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = GeekUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Geek"
        verbose_name_plural = "Geeks"
