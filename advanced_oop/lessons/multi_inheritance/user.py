from saveable import Saveable

class User(Saveable):
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def __repr__(self) -> str:
        return f'User: <{self.username}>'
    
    def login(self) -> str:
        return "Logged in!"
    
    def to_dict(self):
        return {
            'username': self.username,
            'passowrd': self.password
        }