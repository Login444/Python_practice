class User:
    def __init__(self, name: str, u_id: str, level: int):
        self.name = name
        self.u_id = u_id
        self.level = level

    def __str__(self):
        return f'{self.name}, {self.u_id = }, {self.level = }'
