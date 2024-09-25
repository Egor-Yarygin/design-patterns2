from src.core.abstract_model import abstract_model
from src.core.custom_exceptions import argument_exception

class range_model(abstract_model):
    def __init__(self, name: str, conversion_factor: int, base_range=None):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise argument_exception("Наименование единицы измерения должно быть непустой строкой!")
        if not isinstance(conversion_factor, int) or conversion_factor <= 0:
            raise argument_exception("Коэффициент пересчета должен быть положительным целым числом!")
        if base_range is not None and not isinstance(base_range, range_model):
            raise argument_exception("Базовая единица измерения должна быть объектом range_model!")
        
        self.__name = name.strip()
        self.__conversion_factor = conversion_factor
        self.__base_range = base_range

    @property
    def name(self) -> str:
        return self.__name

    @property
    def conversion_factor(self) -> int:
        return self.__conversion_factor

    @property
    def base_range(self):
        return self.__base_range

    def set_compare_mode(self, other_object) -> bool:
        if other_object is None:
            return False
        if not isinstance(other_object, range_model):
            return False
        return self.__name == other_object.name and self.__conversion_factor == other_object.conversion_factor
