import unittest
from src.models.range_model import range_model
from src.custom_exceptions import argument_exception

class TestRangeModel(unittest.TestCase):

    def test_valid_range(self):
        base_range = range_model("грамм", 1)
        new_range = range_model("килограмм", 1000, base_range)
        self.assertEqual(new_range.conversion_factor, 1000)
        self.assertEqual(new_range.base_range.name, "грамм")

    def test_invalid_range(self):
        # Проверка на создание единицы измерения с некорректным именем
        with self.assertRaises(argument_exception):
            range_model("", 1000)
        
        # Проверка на создание единицы измерения с некорректным коэффициентом пересчета
        with self.assertRaises(argument_exception):
            range_model("килограмм", -1000)
        
        # Проверка на создание единицы измерения с некорректной базовой единицей
        with self.assertRaises(argument_exception):
            range_model("килограмм", 1000, base_range="неверный_тип")


if __name__ == '__main__':
    unittest.main()
