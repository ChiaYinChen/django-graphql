from typing import Any

from django.contrib.auth.hashers import make_password

from account.graph.types import UserCreate
from account.models import User as UserModel


class CRUDUser:
    """CRUD operations for user."""

    @classmethod
    async def get_by_email(cls, *, email: str) -> UserModel | None:
        """Get user by email."""
        return await UserModel.objects.filter(email=email).afirst()
