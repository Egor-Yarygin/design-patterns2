import unittest
from src.models.nomenclature_model import nomenclature_model
from src.models.nomenclature_group_model import nomenclature_group_model
from src.models.range_model import range_model
from src.custom_exceptions import argument_exception

class TestNomenclatureModel(unittest.TestCase):

    def test_valid_nomenclature(self):
        group = nomenclature_group_model("Товары")
        range_unit = range_model("кг", 1000)
        nomenclature = nomenclature_model("Номенклатура", "Полное наименование", range_unit, group)
        
        self.assertEqual(nomenclature.nomenclature_group.name, "Товары")
        self.assertEqual(nomenclature.name, "Номенклатура")
        self.assertEqual(nomenclature.full_name, "Полное наименование")
        self.assertEqual(nomenclature.range_unit.name, "кг")
        self.assertEqual(nomenclature.range_unit.conversion_factor, 1000)


    def test_invalid_full_name_length(self):
        group = nomenclature_group_model("Товары")
        unit = range_model("килограмм", 1000, range_model("грамм", 1))

        with self.assertRaises(argument_exception):
            # Полное наименование превышает 255 символов
            long_name = "Т" * 256
            nomenclature_model("Товар 1", long_name, group, unit)

    def test_invalid_group(self):
        range_unit = range_model("кг", 1000)
        with self.assertRaises(argument_exception):
            # Передаем некорректный тип для группы номенклатуры
            nomenclature_model("Номенклатура", "Полное наименование", range_unit, "Неверная группа")


    def test_invalid_unit(self):
        group = nomenclature_group_model("Товары")

        with self.assertRaises(argument_exception):
            # Некорректная единица измерения
            nomenclature_model("Товар 1", "Товар полное наименование", group, None)
