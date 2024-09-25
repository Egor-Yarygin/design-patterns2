import unittest
import unittest.mock
from src.settings_manager import settings_manager
from src.models.organization_model import organization_model
from src.core.custom_exceptions import argument_exception

class TestOrganizationModel(unittest.TestCase):

    def test_valid_organization(self):
        manager = settings_manager()
        manager.open("C:/path/to/settings.json")
        company = organization_model(manager.current_settings)

        self.assertEqual(company.inn, manager.current_settings.inn)
        self.assertEqual(company.bik, manager.current_settings.bik)

    def test_invalid_inn(self):
        # Создаем mock-объект settings
        mock_settings = unittest.mock.Mock()
        mock_settings.inn = "12345"  # Некорректный ИНН
        mock_settings.bik = "123456789"
        mock_settings.account = "12345678901"
        mock_settings.ownership_type = "Частн"

        # Проверка на некорректный ИНН
        with self.assertRaises(argument_exception):
            organization_model(mock_settings)


if __name__ == '__main__':
    unittest.main()
