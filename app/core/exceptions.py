class AppException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class NotFoundException(AppException):
    pass

class ForbiddenException(AppException):
    pass

class ConflictException(AppException):
    pass