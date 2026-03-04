from schemas import CreateUser, BaseUser

users = []

class UserService:
    def __init__(self):
        self.user_mock_db = users

    def add_user(self, new_user: CreateUser):
        for user in self.user_mock_db:
            if user.email == new_user.email:
                return {
                    "status": "Failed",
                    "message": "Email already exists"
                }
            elif user.username == new_user.username:
                return {
                    "status": "Failed",
                    "message": "Username already exists"
                }
            elif user.id == new_user.id:
                return {
                    "status": "Failed",
                    "message": "Id already exists"
                }

        new_user.password = "pass"

        self.user_mock_db.append(new_user)

        return BaseUser(**new_user.model_dump())

    def get_all_users(self):
        print(users)

        return [BaseUser(**user.model_dump()) for user in self.user_mock_db]
