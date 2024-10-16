from typing import Any

from asgiref.sync import sync_to_async
from django.contrib.auth.hashers import make_password

from account.graph.types import UserCreate
from account.models import User as UserModel


class CRUDUser:
    """CRUD operations for user."""

    @classmethod
    async def get_by_email(cls, *, email: str) -> UserModel | None:
        """Retrieve a user instance based on the provided email."""
        return await UserModel.objects.filter(email=email).afirst()

    @classmethod
    async def get_all_instance(cls) -> list[UserModel | None]:
        """Retrieve all instances of the user model."""
        return await sync_to_async(list)(UserModel.objects.all())

    @classmethod
    async def create(cls, *, obj_in: UserCreate | dict[str, Any]) -> UserModel:
        """Create a new user with email and password."""
        if isinstance(obj_in, dict):
            create_data = obj_in.copy()
        else:
            create_data = obj_in.__dict__
        hashed_password = make_password(create_data["password"])
        del create_data["password"]
        db_obj = UserModel(**create_data, password=hashed_password)
        await db_obj.asave()
        return db_obj
