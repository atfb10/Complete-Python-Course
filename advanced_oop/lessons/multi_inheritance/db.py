class Database:
    content = {'users': []}

    @classmethod
    def insert(cls, data) -> None:
        cls.content['users'].append(data)
        return
    
    @classmethod
    def remove(cls, finder) -> None:
        cls.content['users'] = [user for user in cls.content['users'] if not finder(user)]
        return

    @classmethod
    def find(cls, finder) -> list:
        return [user for user in cls.content['users'] if finder(user)]