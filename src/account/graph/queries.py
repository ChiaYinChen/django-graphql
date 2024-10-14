import strawberry
import strawberry_django

from account.graph import types
from account.graph.services import UserService


@strawberry.type
class Query:
    users: list[types.User] = strawberry_django.field()
    user: types.User | None = strawberry_django.field(resolver=UserService.get_user)
