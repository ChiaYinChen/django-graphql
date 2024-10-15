import strawberry
import strawberry_django

from account.graph import types as UserTypes
from account.graph.services import UserService
from utils import exceptions as exc
from utils.constants import CustomErrorCode


@strawberry.type
class UserMutations:

    @strawberry_django.mutation
    async def create(self, user_in: UserTypes.UserCreate) -> UserTypes.User:
        user = await UserService.get_user(email=user_in.email)
        if user:
            raise exc.ConflictError(CustomErrorCode.ENTITY_CONFLICT, "Email already registered")
        return await UserService.create_user(obj_in=user_in)


@strawberry.type
class Mutation:

    @strawberry.field
    def user(self) -> UserMutations:
        return UserMutations()
