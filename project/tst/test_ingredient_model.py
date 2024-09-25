import unittest
from src.models.ingredient_model import ingredient_model
from src.models.nomenclature_model import nomenclature_model
from src.models.range_model import range_model
from src.models.nomenclature_group_model import nomenclature_group_model
from src.core.custom_exceptions import argument_exception

class TestIngredientModel(unittest.TestCase):

    def test_valid_ingredient(self):
        group = nomenclature_group_model("Товары")
        range_unit = range_model("кг", 1000)
        nomenclature = nomenclature_model("Номенклатура", "Полное наименование", range_unit, group)
        ingredient = ingredient_model(nomenclature.name, 200, "кг")
        
        self.assertEqual(ingredient.name, nomenclature.name)
        self.assertEqual(ingredient.quantity, 200)
        self.assertEqual(ingredient.unit, "кг")

    def test_invalid_quantity(self):
        group = nomenclature_group_model("Товары")
        range_unit = range_model("кг", 1000)
        nomenclature = nomenclature_model("Номенклатура", "Полное наименование", range_unit, group)
        with self.assertRaises(argument_exception):
            # Передаем отрицательное количество и единицу измерения
            ingredient_model(nomenclature.name, -50, "кг")

if __name__ == '__main__':
    unittest.main()
