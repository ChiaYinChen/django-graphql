from datetime import datetime

import strawberry
import strawberry.tools

from account.graph import mutations as user_mutations
from account.graph import queries as user_queries
from utils.formatter import DATETIME_FORMATTED

__all__ = ("schema",)

query = strawberry.tools.merge_types(
    "Query",
    (user_queries.Query,),
)
mutation = strawberry.tools.merge_types(
    "Mutation",
    (user_mutations.Mutation,),
)

schema = strawberry.Schema(query=query, mutation=mutation, scalar_overrides={datetime: DATETIME_FORMATTED})
