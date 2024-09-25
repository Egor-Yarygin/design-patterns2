from src.core.abstract_logic import abstract_logic
from src.data_reposity import data_reposity
from src.core.custom_exceptions import validator
from src.models.nomenclature_group_model import nomenclature_group_model
from src.models.range_model import range_model
from src.models.nomenclature_model import nomenclature_model
from src.settings_manager import settings_manager
from src.settings import settings
from src.models.recipe_model import recipe_model
from src.models.ingredient_model import ingredient_model

class start_service(abstract_logic):
    __reposity: data_reposity = None
    __settings_manager: settings_manager = None

    def __init__(self, reposity: data_reposity, manager: settings_manager ) -> None:
        super().__init__()
        validator.validate(reposity, data_reposity)
        validator.validate(manager, settings_manager)
        self.__reposity = reposity
        self.__settings_manager = manager

    @property 
    def settings(self) -> settings:
        return self.__settings_manager.settings

    def __create_nomenclature_groups(self):
        groups = []
        groups.append(nomenclature_group_model.default_group_cold())
        groups.append(nomenclature_group_model.default_group_source())
        self.__reposity.data[data_reposity.group_key()] = groups

    def __create_units_of_measure(self):
        units = []
        units.append(range_model("грамм", 1))  # базовая единица измерения
        units.append(range_model("килограмм", 1000, units[0]))  # коэффициент пересчета
        self.__reposity.data['units'] = units

    def __create_nomenclature(self):
        nomenclature = []
        group = self.__reposity.data[data_reposity.group_key()][0]  # Используем первую группу
        unit = self.__reposity.data['units'][0]  # Используем первую единицу измерения
        nomenclature.append(nomenclature_model("Товар 1", "Полное наименование Товар 1", unit, group))
        self.__reposity.data['nomenclature'] = nomenclature

    def create(self):
        self.__create_nomenclature_groups()
        self.__create_units_of_measure()
        self.__create_nomenclature()

    def set_exception(self, ex: Exception):
        self._inner_set_exception(ex)

    def __create_receipts(self):
        receipts = []
        

        # Ингредиенты для рецепта с занятия
        ingredients1 = [
            ingredient_model("Мука", 100, "гр"),
            ingredient_model("Сахар", 80, "гр"),
            ingredient_model("Масло", 70, "гр"),
            ingredient_model("Яйца", 1, "шт"),
            ingredient_model("Ванилин", 5, "гр")
        ]
        receipt1 = recipe_model("Вафли хрустящие", ingredients1, "20 мин")
        
        # Ингредиенты для собственного рецепта
        ingredients2 = [
            ingredient_model("Мука", 250, "гр"),
            ingredient_model("Сахар", 200, "гр"),
            ingredient_model("Масло", 150, "гр"),
            ingredient_model("Яйца", 3, "шт"),
            ingredient_model("Разрыхлитель", 5, "гр")
        ]
        receipt2 = recipe_model("Собственный рецепт торта", ingredients2, "45 мин")
        
        receipts.extend([receipt1, receipt2])
        self.__reposity.data['receipts'] = receipts