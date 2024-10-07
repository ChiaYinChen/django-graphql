from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from account.managers import CustomUserManager
from utils.models import BaseModel


class User(AbstractBaseUser, BaseModel):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        db_table = "USER"
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return self.email
