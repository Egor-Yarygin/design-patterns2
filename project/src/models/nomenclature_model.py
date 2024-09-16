from src.abstract_model import abstract_model
from src.custom_exceptions import argument_exception
from src.models.range_model import range_model
from src.models.nomenclature_group_model import nomenclature_group_model

class nomenclature_model(abstract_model):
    def __init__(self, name: str, full_name: str, range_unit: range_model, nomenclature_group: nomenclature_group_model):
        if len(name) > 50:
            raise argument_exception("Наименование не может превышать 50 символов!")
        if len(full_name) > 255:
            raise argument_exception("Полное наименование не может превышать 255 символов!")
        if not isinstance(nomenclature_group, nomenclature_group_model):
            raise argument_exception("Неверный тип для группы номенклатуры!")
        
        self.__name = name
        self.__full_name = full_name
        self.__range_unit = range_unit
        self.__nomenclature_group = nomenclature_group

    @property
    def name(self) -> str:
        return self.__name

    @property
    def full_name(self) -> str:
        return self.__full_name

    @property
    def range_unit(self) -> range_model:
        return self.__range_unit

    @property
    def nomenclature_group(self) -> nomenclature_group_model:
        return self.__nomenclature_group

    def set_compare_mode(self, other_object) -> bool:
        if other_object is None:
            return False
        if not isinstance(other_object, nomenclature_model):
            return False
        return self.__name == other_object.name
