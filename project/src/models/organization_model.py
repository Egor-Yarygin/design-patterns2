from src.core.abstract_model import abstract_model
from src.core.custom_exceptions import argument_exception
from src.settings import settings

class organization_model(abstract_model):
    def __init__(self, settings: settings):
        if len(settings.inn) != 12:
            raise argument_exception("ИНН должен состоять из 12 символов!")
        if len(settings.bik) != 9:
            raise argument_exception("БИК должен состоять из 9 символов!")
        if len(settings.account) != 11:
            raise argument_exception("Счет должен состоять из 11 символов!")
        if len(settings.ownership_type) > 5:
            raise argument_exception("Форма собственности не должна превышать 5 символов!")

        self.__inn = settings.inn
        self.__bik = settings.bik
        self.__account = settings.account
        self.__ownership_type = settings.ownership_type
        self.__organization_name = settings.organization_name

    @property
    def inn(self) -> str:
        return self.__inn

    @property
    def bik(self) -> str:
        return self.__bik

    @property
    def account(self) -> str:
        return self.__account

    @property
    def ownership_type(self) -> str:
        return self.__ownership_type

    @property
    def organization_name(self) -> str:
        return self.__organization_name

    def set_compare_mode(self, other_object) -> bool:
        if other_object is None:
            return False
        if not isinstance(other_object, organization_model):
            return False
        return self.__inn == other_object.inn
