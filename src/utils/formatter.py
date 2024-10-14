from datetime import datetime

import strawberry
from django.conf import settings


class DateTime:
    """
    Serialize and parse datetime values using the specified Taiwan's timezone format.
    DATE_TIME_FORMAT: %Y-%m-%d %H:%M:%S
    """

    @staticmethod
    def serialize(value: datetime) -> str:
        """Format datetime as a string."""
        return value.strftime(settings.DATE_TIME_FORMAT)

    @staticmethod
    def parse_value(value: str) -> datetime:
        """Parse string back into a datetime object."""
        return datetime.strptime(value, settings.DATE_TIME_FORMAT)


# define a custom scalar for datetime formatted to Taiwan's timezone
DATETIME_FORMATTED = strawberry.scalar(
    datetime,
    name="datetime",
    description="Custom scalar for datetime formatted to Taiwan's timezone",
    serialize=DateTime.serialize,
    parse_value=DateTime.parse_value,
)
