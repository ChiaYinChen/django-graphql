from datetime import datetime

import strawberry
import strawberry.tools

from account.graph.queries import UserQuery
from utils.formatter import DATETIME_FORMATTED

__all__ = ("schema",)

query = strawberry.tools.merge_types(
    "Query",
    (UserQuery,),
)

schema = strawberry.Schema(query=query, scalar_overrides={datetime: DATETIME_FORMATTED})
