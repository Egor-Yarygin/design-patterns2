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


"""
Набор проверок данных
"""
class validator:

    @staticmethod
    def validate( value, type_, len_= None):
        """
            Валидация аргумента по типу и длине
        Args:
            value (any): Аргумент
            type_ (object): Ожидаемый тип
            len_ (int): Максимальная длина
        Raises:
            arguent_exception: Некорректный тип
            arguent_exception: Неулевая длина
            arguent_exception: Некорректная длина аргумента
        Returns:
            True или Exception
        """

        if value is None:
            raise argument_exception("Пустой аргумент")

        # Проверка типа
        if not isinstance(value, type_):
            raise argument_exception("Некорректный тип")

        # Проверка аргумента
        if len(str(value).strip()) == 0:
            raise argument_exception("Пустой аргумент")

        if len_ is not None and len(str(value).strip()) >= len_:
            raise argument_exception("Некорректная длина аргумента")

        return True
