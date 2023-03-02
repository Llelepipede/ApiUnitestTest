class GameDBException(Exception):
    ...


class GameDBNotFound(GameDBException):
    def __init__(self):
        self.status_code = 404
        self.detail = "Game Not Found"


class GamesDBAlreadyExist(GameDBException):
    def __init__(self):
        self.status_code = 409
        self.detail = "Game Already Exists"