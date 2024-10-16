from typing import Generic, TypeVar

import strawberry

from utils.paginations import PaginationWindow

ModelType = TypeVar("ModelType")


@strawberry.type
class GenericResponse(Generic[ModelType]):
    """Generic wrapper for API responses."""

    message: str | None = None
    data: ModelType | None = None


@strawberry.type
class GenericListResponse(Generic[ModelType]):
    """Generic wrapper for API responses for query list data with pagination."""

    message: str | None = None
    data: list[ModelType] | None = None
    paging: PaginationWindow | None = None
