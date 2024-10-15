from account.graph.repositories import CRUDUser
from account.graph.types import UserCreate
from account.models import User as UserModel


class UserService:
    @classmethod
    async def get_user(cls, email: str) -> UserModel | None:
        return await CRUDUser.get_by_email(email=email)

    @classmethod
    async def create_user(cls, obj_in: UserCreate) -> UserModel:
        return await CRUDUser.create(obj_in=obj_in)
