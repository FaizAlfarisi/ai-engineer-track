class ApiError(Exception):
    def __init__(self, message: str, status: int | None = None):
        self.message = message
        self.status = status
        super().__init__(message)

class BadRequestError(Exception):
    pass

class CorruptDataError(Exception):
    pass