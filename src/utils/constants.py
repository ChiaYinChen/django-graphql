from enum import Enum


class CustomErrorCode(int, Enum):

    # entity errors
    ENTITY_CONFLICT = 1001                        # Conflict between entities in the system
    ENTITY_NOT_FOUND = 1002                       # Entity not found

    # format errors
    REQUIRED_FIELD_MISSING = 6001                 # Required field is missing
    INVALID_EMAIL = 6002                          # Invalid email address format
    INVALID_MIN_LENGTH = 6003                     # Value does not meet the minimum length requirement
    INVALID_MAX_LENGTH = 6004                     # Value exceeds the maximum length allowed

    # validation errors
    VALIDATE_ERROR = 9100                         # General validation error
