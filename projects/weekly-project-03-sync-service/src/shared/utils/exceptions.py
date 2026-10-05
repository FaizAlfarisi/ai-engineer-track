class ApiError(Exception):
    def __init__(self, message: str, status: int | None = None):
        super().__init__(message)
        self.message = message
        self.status = status

class BadRequestError(Exception):
    pass

class CorruptDataError(Exception):
    pass