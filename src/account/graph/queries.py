import strawberry
import strawberry_django

from account.graph import types


@strawberry.type
class UserQuery:
    users: list[types.User] = strawberry_django.field()
    user: types.User | None = strawberry_django.field()
