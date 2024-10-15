from django.http import HttpRequest
from strawberry.django.views import AsyncGraphQLView
from strawberry.http import GraphQLHTTPResponse
from strawberry.types import ExecutionResult

from utils.constants import CustomErrorCode
from utils.exceptions import CustomError


class CustomAsyncGraphQLView(AsyncGraphQLView):

    async def process_result(self, request: HttpRequest, result: ExecutionResult) -> GraphQLHTTPResponse:
        data: GraphQLHTTPResponse = {"data": result.data}

        if result.errors:
            for err in result.errors:
                if isinstance(err.original_error, CustomError):
                    custom_error = err.original_error
                    data["errors"] = [
                        {
                            "error_code": custom_error.error_code,
                            "message": custom_error.message,
                        }
                    ]
                else:
                    data["errors"] = err.formatted
                    data["errors"]["error_code"] = CustomErrorCode.VALIDATE_ERROR.value

        return data
