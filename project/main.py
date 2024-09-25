from src.settings_manager import settings_manager

# Тестирование
def main():
    manager1 = settings_manager()
    if not manager1.open("C:/Users/Costo/OneDrive/Документы/GitHub/design-patterns2/project/data/settings1.json"):
        print("Настройки не загружены!")

    print(f"""\nsettings1:
        Наименование: {manager1.current_settings.organization_name} 
        ИНН: {manager1.current_settings.inn} 
        Счёт: {manager1.current_settings.account}
        Корреспондентский счёт: {manager1.current_settings.correspondent_account}
        БИК: {manager1.current_settings.bik}
        Вид собственности: {manager1.current_settings.ownership_type}""")

    # Создание второго экземпляра для проверки
    manager2 = settings_manager()

    print(f"""\nsettings2:
        Наименование: {manager2.current_settings.organization_name} 
        ИНН: {manager2.current_settings.inn} 
        Счёт: {manager2.current_settings.account}
        Корреспондентский счёт: {manager2.current_settings.correspondent_account}
        БИК: {manager2.current_settings.bik}
        Вид собственности: {manager2.current_settings.ownership_type}""")


if __name__ == "__main__":
    main()
