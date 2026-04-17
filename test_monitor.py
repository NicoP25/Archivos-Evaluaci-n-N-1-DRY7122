import unittest
from monitor import get_device_data

class TestSDNMonitor(unittest.TestCase):
    
    def test_data_type(self):
        resultado = get_device_data(1)
        self.assertIsInstance(resultado, dict)

    def test_attribute_integrity(self):
        resultado = get_device_data(1)
        self.assertIn('username', resultado)

    def test_expected_value(self):
        resultado = get_device_data(1)
        self.assertEqual(resultado['username'], 'Bret')

if __name__ == '__main__':
    unittest.main()

