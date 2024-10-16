import strawberry
import strawberry_django

from account.graph import types
from account.graph.services import UserService
from utils.paginations import PaginationParams, get_paginated_response
from utils.responses import GenericListResponse, GenericResponse


@strawberry.type
class UserQueries:
    """User queryset that provides fields to access user-related data."""

    @strawberry_django.field
    async def all(self, paging: PaginationParams) -> GenericListResponse[types.User]:
        """
        Retrieve a paginated list of users.
        """
        dataset = await UserService.get_users()
        page_info, users = get_paginated_response(dataset, paging_params=paging)
        return GenericListResponse(data=users, paging=page_info)

    @strawberry_django.field
    async def single(self, email: str) -> GenericResponse[types.User]:
        """
        Retrieve a user by email.
        """
        user = await UserService.get_user(email=email)
        return GenericResponse(data=user)


@strawberry.type
class Query:
    """Root query class for user-related queries."""

    @strawberry.field
    def user(self) -> UserQueries:
        return UserQueries()
