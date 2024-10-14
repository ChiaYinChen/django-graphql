from datetime import datetime

import strawberry
import strawberry.tools

from account.graph import queries as user_queries
from utils.formatter import DATETIME_FORMATTED

__all__ = ("schema",)

query = strawberry.tools.merge_types(
    "Query",
    (user_queries.Query,),
)

schema = strawberry.Schema(query=query, scalar_overrides={datetime: DATETIME_FORMATTED})
