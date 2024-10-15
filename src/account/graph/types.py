import strawberry_django
from strawberry import auto

from account import models
from utils.formatter import DATETIME_FORMATTED


@strawberry_django.type(models.User)
class UserBase:
    email: auto


@strawberry_django.input(models.User)
class UserCreate(UserBase):
    password: str


@strawberry_django.type(models.User)
class User(UserBase):
    id: auto
    created_at: DATETIME_FORMATTED
    updated_at: DATETIME_FORMATTED
