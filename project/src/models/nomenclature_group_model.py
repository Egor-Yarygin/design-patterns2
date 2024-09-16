from src.abstract_model import abstract_model
from src.custom_exceptions import argument_exception

class nomenclature_group_model(abstract_model):
    def __init__(self, name: str):
        if not name or len(name.strip()) == 0:
            raise argument_exception("Наименование не может быть пустым!")
        if len(name) > 50:
            raise argument_exception("Наименование не может превышать 50 символов!")
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name

    def set_compare_mode(self, other_object) -> bool:
        if other_object is None:
            return False
        if not isinstance(other_object, nomenclature_group_model):
            return False
        return self.__name == other_object.name
