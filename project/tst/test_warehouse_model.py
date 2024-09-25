import unittest
from src.models.warehouse_model import warehouse_model
from src.core.custom_exceptions import argument_exception

class TestWarehouseModel(unittest.TestCase):

    def test_valid_warehouse(self):
        warehouse = warehouse_model("Основной склад", "SKL001")
        self.assertEqual(warehouse.name, "Основной склад")
        self.assertEqual(warehouse.code, "SKL001")

    def test_invalid_warehouse_name(self):
        with self.assertRaises(argument_exception):
            warehouse_model("Очень длинное название склада, которое превышает 50 символов", "SKL001")

    def test_invalid_warehouse_code(self):
        with self.assertRaises(argument_exception):
            warehouse_model("Склад", "Очень длинный код")

if __name__ == '__main__':
    unittest.main()
