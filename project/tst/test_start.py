from src.settings_manager import settings_manager
from src.start_service import start_service
from src.data_reposity import data_reposity
import unittest


"""
Набор тестов для проверки работы старта приложения
"""
class test_settings(unittest.TestCase):
    
    """
    Проверить создание инстанса start_service
    """
    def test_create_start_service(self):
        # Подготовка
        manager = settings_manager()
        manager.open("C:/Users/Costo/OneDrive/Документы/GitHub/design-patterns2/project/data/settings1.json")
        reposity = data_reposity()

        # Действие
        start = start_service(reposity, manager)

        # Проверки
        assert start is not None



