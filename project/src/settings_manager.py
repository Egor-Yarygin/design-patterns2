import json
import os
from src.settings import settings
from src.abstract_logic import abstract_logic
from src.core.custom_exceptions import validator

"""
Менеджер настроек
"""
class settings_manager(abstract_logic):
    __file_name = "C:/Users/Costo/OneDrive/Документы/GitHub/design-patterns/project/data/settings.json"
    __settings: settings = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(settings_manager, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        if self.__settings is None:
            self.__settings = self.__default_setting()

    """
    Открыть и загрузить настройки
    """
    def open(self, file_name: str = ""):
        validator.validate(file_name, str)

        if file_name != "":
            self.__file_name = file_name

        try:
            full_name = os.path.abspath(self.__file_name)
            with open(full_name, encoding='utf-8') as stream:
                data = json.load(stream)

            self.__settings = self.convert(data)
            return True
        except TypeError as t:
            print(f"Ошибка типа данных: {t}")
            return False
        except ValueError as v:
            print(f"Ошибка данных настроек: {v}")
            return False
        except Exception as e:
            print(f"Ошибка загрузки файла настроек: {e}")
            self.__settings = self.__default_setting()
            self.set_exception(e)
            return False

    """
    Конвертация словаря в объект settings
    """
    def convert(self, data: dict):
        new_settings = settings()
        fields = list(filter(lambda x: not x.startswith("_"), dir(settings)))

        for field in fields:
            if field in data:
                value = data[field]
                setattr(new_settings, field, value)

        return new_settings

    """
    Загруженные настройки
    """
    @property
    def current_settings(self)->settings:
        return self.__settings

    """
    Набор настроек по умолчанию
    """
    def __default_setting(self):
        data = settings()
        data.inn = "380(default)"
        data.organization_name = "Рога и копыта (default)"
        data.account = "12(default)"
        data.correspondent_account = "12(default)"
        data.bik = "(default)"
        data.ownership_type = "(def)"
        return data
    
    def set_exception(self, e: Exception):
        self._inner_set_exception(e)