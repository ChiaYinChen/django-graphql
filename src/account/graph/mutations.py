import strawberry
import strawberry_django

from account.graph import types
from account.graph.services import UserService
from utils import exceptions as exc
from utils.constants import CustomErrorCode
from utils.responses import GenericResponse


@strawberry.type
class UserMutations:
    """User mutation that handles user-related operations."""

    @strawberry_django.mutation
    async def create(self, user_in: types.UserCreate) -> GenericResponse[types.User]:
        """
        Create a new user.
        """
        user = await UserService.get_user(email=user_in.email)
        if user:
            raise exc.ConflictError(CustomErrorCode.ENTITY_CONFLICT, "Email already registered")
        user = await UserService.create_user(obj_in=user_in)
        return GenericResponse(data=user)


@strawberry.type
class Mutation:
    """Root mutation class for user-related operations."""

    @strawberry.field
    def user(self) -> UserMutations:
        return UserMutations()
