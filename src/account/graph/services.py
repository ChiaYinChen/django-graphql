from account.graph.repositories import CRUDUser
from account.graph.types import UserCreate
from account.models import User as UserModel


class UserService:
    """User management service."""

    @classmethod
    async def get_users(cls) -> list[UserModel | None]:
        return await CRUDUser.get_all_instance()

    @classmethod
    async def get_user(cls, email: str) -> UserModel | None:
        return await CRUDUser.get_by_email(email=email)

    @classmethod
    async def create_user(cls, obj_in: UserCreate) -> UserModel:
        """
        Register a new user.

        This method is used to register a new user with anonymous access.
        """
        return await CRUDUser.create(obj_in=obj_in)
