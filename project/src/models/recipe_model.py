from src.abstract_model import abstract_model
from src.core.custom_exceptions import argument_exception

class recipe_model(abstract_model):
    def __init__(self, name: str, ingredients: list, preparation_time: str):
        if len(name) > 100:
            raise argument_exception("Наименование рецепта не может превышать 100 символов!")
        if len(ingredients) == 0:
            raise argument_exception("Список ингредиентов не может быть пустым!")
        if not preparation_time:
            raise argument_exception("Время приготовления должно быть указано!")
        
        self.__name = name
        self.__ingredients = ingredients
        self.__preparation_time = preparation_time

    @property
    def name(self) -> str:
        return self.__name

    @property
    def ingredients(self) -> list:
        return self.__ingredients

    @property
    def preparation_time(self) -> str:
        return self.__preparation_time

    def set_compare_mode(self, other_object) -> bool:
        if other_object is None:
            return False
        if not isinstance(other_object, recipe_model):
            return False
        return self.__name == other_object.name
