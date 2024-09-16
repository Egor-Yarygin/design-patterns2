import unittest
from models.range_model import range
from models.nomenclature_model import nomenclature

"""
Набор тестов для проверки работы моделей
"""
class test_models(unittest.TestCase):

    """
    Проверить вариант сравнения (по коду)
    """
    def test_nomenclature_model(self):
        # Подготовка
        item1 = nomenclature()
        item1.name = "test1"

        item2 = nomenclature()
        item2.name = "test1"

        # Проверка
        assert item1 != item2


    """
    Проверить вариант сравнения (по наименованию)
    """
    def test_range_model(self):
        # Подготовка
        item1 = range()
        item1.name = "test1"

        item2 = range()
        item2.name = "test1"

        # Проверка
        assert item1 == item2