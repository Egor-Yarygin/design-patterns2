from src.core.abstract_model import abstract_model
from src.core.custom_exceptions import argument_exception
from src.core.base_models import base_model_name

class nomenclature_group_model(base_model_name):
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
    
        """
    Default группа - сырье (фабричный метод)
    """
    @staticmethod
    def default_group_source():
        item = nomenclature_group_model()
        item.name = "Сырье"
        return item
    
    """
    Default группа - замарозка (фабричный метод)
    """
    @staticmethod
    def default_group_cold():
        item = nomenclature_group_model()
        item.name = "Заморозка"
        return item
    
