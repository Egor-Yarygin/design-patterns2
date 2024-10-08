"""
Настройки
"""
class settings:
    __organization_name = ""
    __inn = ""
    __account = ""
    __correspondent_account = ""
    __bik = ""
    __ownership_type = ""

    @property
    def organization_name(self):
        return self.__organization_name

    @organization_name.setter
    def organization_name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Некорректно передан параметр!")
        self.__organization_name = value

    @property
    def inn(self):
        return self.__inn

    @inn.setter
    def inn(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Некорректно переданы параметры!")
        if len(value) != 12:
            raise ValueError("ИНН должен состоять из 12 символов!")
        self.__inn = value

    @property
    def account(self):
        return self.__account

    @account.setter
    def account(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Некорректно переданы параметры!")
        if len(value) != 11:
            raise ValueError("Счёт должен состоять из 11 символов!")
        self.__account = value

    @property
    def correspondent_account(self):
        return self.__correspondent_account

    @correspondent_account.setter
    def correspondent_account(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Некорректно переданы параметры!")
        if len(value) != 11:
            raise ValueError("Корреспондентский счёт должен состоять из 11 символов!")
        self.__correspondent_account = value

    @property
    def bik(self):
        return self.__bik

    @bik.setter
    def bik(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Некорректно переданы параметры!")
        if len(value) != 9:
            raise ValueError("БИК должен состоять из 9 символов!")
        self.__bik = value

    @property
    def ownership_type(self):
        return self.__ownership_type

    @ownership_type.setter
    def ownership_type(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Некорректно переданы параметры!")
        if len(value) != 5:
            raise ValueError("Вид собственности должен состоять из 5 символов!")
        self.__ownership_type = value
