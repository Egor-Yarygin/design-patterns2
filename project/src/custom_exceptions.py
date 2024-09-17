class BaseCustomException(Exception):
    """Базовое исключение для всех кастомных ошибок"""
    def __init__(self, message):
        super().__init__(message)


class argument_exception(BaseCustomException):
    """Исключение для некорректных аргументов"""
    def __init__(self, message="Некорректный аргумент передан"):
        super().__init__(message)


class operation_exception(BaseCustomException):
    """Исключение для некорректных операций"""
    def __init__(self, message="Некорректная операция"):
        super().__init__(message)


class error_proxy(BaseCustomException):
    """Исключение для общих ошибок"""
    def __init__(self, message="Произошла ошибка"):
        super().__init__(message)
