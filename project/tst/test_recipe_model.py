import unittest
from src.models.recipe_model import recipe_model
from src.models.ingredient_model import ingredient_model
from src.models.nomenclature_model import nomenclature_model
from src.models.range_model import range_model
from src.models.nomenclature_group_model import nomenclature_group_model
from src.core.custom_exceptions import argument_exception

class TestRecipeModel(unittest.TestCase):

    def test_valid_recipe(self):
        group = nomenclature_group_model("Товары")
        range_unit = range_model("кг", 1000)
        nomenclature = nomenclature_model("Номенклатура", "Полное наименование", range_unit, group)
        ingredient = ingredient_model(nomenclature.name, 500, "кг")
        recipe = recipe_model("Тестовый рецепт", [ingredient], "30 мин")

        self.assertEqual(recipe.name, "Тестовый рецепт")
        self.assertEqual(len(recipe.ingredients), 1)
        self.assertEqual(recipe.ingredients[0].name, nomenclature.name)
        self.assertEqual(recipe.preparation_time, "30 мин")

    def test_invalid_recipe_name(self):
        group = nomenclature_group_model("Товары")
        range_unit = range_model("кг", 1000)
        nomenclature = nomenclature_model("Номенклатура", "Полное наименование", range_unit, group)
        ingredient = ingredient_model(nomenclature.name, 500, "кг")
        
        with self.assertRaises(argument_exception):
            # Тестируем создание рецепта с некорректным именем
            long_name = "Т" * 101  # Имя превышает 100 символов
            recipe_model(long_name, [ingredient], "30 мин")

    def test_empty_ingredients(self):
        with self.assertRaises(argument_exception):
            # Тестируем создание рецепта с пустым списком ингредиентов
            recipe_model("Пустой рецепт", [], "10 минут")  


if __name__ == '__main__':
    unittest.main()
