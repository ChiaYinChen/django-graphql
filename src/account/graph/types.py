import re
from dataclasses import dataclass

import strawberry
import strawberry_django

from account import models
from utils import exceptions as exc
from utils.constants import CustomErrorCode


@strawberry_django.type(models.User)
class UserBase:
    email: strawberry.auto


@dataclass
@strawberry_django.input(models.User)
class UserCreate(UserBase):
    password: str = strawberry.field(description="Password must be at least 6 characters.")

    def __post_init__(self):
        """
        Validate data after instantiation.

        1. Check if the email format is valid.
        2. Ensure the password is at least 6 characters.
        """
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if re.match(email_pattern, self.email) is None:
            raise exc.BadRequestError(CustomErrorCode.INVALID_EMAIL, "Invalid email format")
        if len(self.password) < 6:
            raise exc.BadRequestError(CustomErrorCode.INVALID_MIN_LENGTH, "Password must be at least 6 characters")


@strawberry_django.type(models.User)
class User(UserBase):
    id: strawberry.auto
    created_at: strawberry.auto
    updated_at: strawberry.auto
