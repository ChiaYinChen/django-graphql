from account.graph.repositories import CRUDUser


class UserService:
    @classmethod
    async def get_user(cls, email: str):
        return await CRUDUser.get_by_email(email=email)
