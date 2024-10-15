import strawberry
import strawberry_django

from account.graph import types as UserTypes
from account.graph.services import UserService


@strawberry.type
class Mutation:
    @strawberry_django.mutation
    async def create(self, user_in: UserTypes.UserCreate) -> UserTypes.User:
        return await UserService.create_user(obj_in=user_in)
