from user import User

class Admin(User):
    def __init__(self, username: str, password: str, access_level: str):
        super(Admin, self).__init__(username, password)
        self.access_level = access_level

    def __repr__(self) -> str:
        return f'User <{self.username}> has access level of <{self.access_level}>'
    
    def to_dict(self) -> dict:
        return {
            'username': self.username,
            'password': self.password,
            'access_level': self.access_level
        }
    
    # self.save() will be searched in Admin
    # then in User
    # then in Saveable where it will be found

    # self.save() uses self.to_dict()
    # self.to_dict() searches in Admin where it will be found

