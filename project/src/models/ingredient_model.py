from src.abstract_model import abstract_model
from src.core.custom_exceptions import argument_exception

class ingredient_model(abstract_model):
    def __init__(self, name: str, quantity: float, unit: str):
        if len(name) > 50:
            raise argument_exception("Наименование ингредиента не может превышать 50 символов!")
        if quantity <= 0:
            raise argument_exception("Количество ингредиента должно быть больше 0!")
        if len(unit) > 20:
            raise argument_exception("Наименование единицы измерения не может превышать 20 символов!")
        
        self.__name = name
        self.__quantity = quantity
        self.__unit = unit

    @property
    def name(self) -> str:
        return self.__name

    @property
    def quantity(self) -> float:
        return self.__quantity

    @property
    def unit(self) -> str:
        return self.__unit

    def set_compare_mode(self, other_object) -> bool:
        if other_object is None:
            return False
        if not isinstance(other_object, ingredient_model):
            return False
        return self.__name == other_object.name and self.__quantity == other_object.quantity and self.__unit == other_object.unit
