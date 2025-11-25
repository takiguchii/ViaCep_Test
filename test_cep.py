from unittest import TestCase
from cep import Cep


class CepTest(TestCase):
    
    
    def test_raise_exception_when_cep_is_wrong(self):
        with self.assertRaises(Exception):
            Cep.from_str('aaaaaaaaaaaaa')
        with self.assertRaises(Exception):
            Cep.from_str('bbbbbbbbbbbbb')
            
    def test_raise_exception_when_is_too_big(self):
        with self.assertRaises(Exception):
            Cep.from_str('111111111')
            
    def test_raise_exception_when_is_too_small(self):
        with self.assertRaises(Exception):
            Cep.from_str('111111')
            
    def test_create_cep(self):
        cep = Cep.from_str('17500-000')
        self.assertIsInstance(cep, Cep)
        self.assertEqual(cep.value, '17500000')
        
    def test_format_cep(self):
        cep = Cep('17500000')
        formatted_cep = cep.formatted()
        self.assertEqual(formatted_cep, '17500-000')