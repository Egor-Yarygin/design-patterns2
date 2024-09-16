from settings_manager import settings_manager

# Тестирование
def main():
    manager1 = settings_manager()
    if not manager1.open("C:/Users/Costo/Documents/training/Design-patterns/project/data/settings1.json"):
        print("Настройки не загружены!")

    print(f"""\nsettings1:
        Наименование: {manager1.settings.organization_name} 
        ИНН: {manager1.settings.inn} 
        Счёт: {manager1.settings.account}
        Корреспондентский счёт: {manager1.settings.correspondent_account}
        БИК: {manager1.settings.bik}
        Вид собственности: {manager1.settings.ownership_type}""")

    # Создание второго экземпляра для проверки
    manager2 = settings_manager()

    print(f"""\nsettings2:
        Наименование: {manager2.settings.organization_name} 
        ИНН: {manager2.settings.inn} 
        Счёт: {manager2.settings.account}
        Корреспондентский счёт: {manager2.settings.correspondent_account}
        БИК: {manager2.settings.bik}
        Вид собственности: {manager2.settings.ownership_type}""")

if __name__ == "__main__":
    main()
