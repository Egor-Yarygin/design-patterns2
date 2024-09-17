import unittest
from src.models.nomenclature_group_model import nomenclature_group_model
from src.custom_exceptions import argument_exception

class TestNomenclatureGroupModel(unittest.TestCase):

    def test_valid_group(self):
        group = nomenclature_group_model("Товары")
        self.assertEqual(group.name, "Товары")

    def test_invalid_name_length(self):
        with self.assertRaises(argument_exception):
            # Наименование группы превышает 50 символов
            long_name = "Т" * 51
            nomenclature_group_model(long_name)

    def test_empty_name(self):
        with self.assertRaises(argument_exception):
            # Наименование группы не может быть пустым
            nomenclature_group_model("")
