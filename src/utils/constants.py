from enum import Enum


class CustomErrorCode(int, Enum):

    # entity errors
    ENTITY_CONFLICT = 1001                        # Conflict between entities in the system
    ENTITY_NOT_FOUND = 1002                       # Entity not found

    # validation errors
    VALIDATE_ERROR = 9100                         # General validation error
