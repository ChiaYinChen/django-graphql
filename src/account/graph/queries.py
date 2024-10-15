import strawberry
import strawberry_django

from account.graph import types
from account.graph.services import UserService


@strawberry.type
class UserQueries:
    """User queryset that provides fields to access user-related data."""

    all: list[types.User] = strawberry_django.field(UserService.get_users)
    single: types.User | None = strawberry_django.field(resolver=UserService.get_user)


@strawberry.type
class Query:
    """Root query class for user-related queries."""

    @strawberry.field
    def user(self) -> UserQueries:
        return UserQueries()
