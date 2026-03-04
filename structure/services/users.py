from schemas import CreateUser, BaseUser

users = []

class UserService:
    def __init__(self):
        self.user_mock_db = users

    def add_user(self, user: CreateUser):
        user.password = "pass"

        self.user_mock_db.append(user)

        return BaseUser(**user.model_dump())

    def get_all_users(self):
        return [BaseUser(**user.model_dump()) for user in self.user_mock_db]

