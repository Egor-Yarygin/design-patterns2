from src.core.abstract_model import abstract_model
from src.core.custom_exceptions import argument_exception

class warehouse_model(abstract_model):
    def __init__(self, name: str, code: str):
        if len(name) > 50:
            raise argument_exception("Наименование склада не может превышать 50 символов!")
        if len(code) > 10:
            raise argument_exception("Код склада не может превышать 10 символов!")

        self.__name = name
        self.__code = code

    @property
    def name(self) -> str:
        return self.__name

    @property
    def code(self) -> str:
        return self.__code

    def set_compare_mode(self, other_object) -> bool:
        if other_object is None:
            return False
        if not isinstance(other_object, warehouse_model):
            return False
        return self.__code == other_object.code
