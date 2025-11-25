from unittest import TestCase
from cep import Cep

# Testes unitários para a classe Cep

class CepTest(TestCase):
    
    # 1. Testa se o CEP é criado corretamente e sem o hífen.
    def test_create_valid_cep(self):
        cep = Cep.from_str('17500-000')
        self.assertIsInstance(cep, Cep)
        self.assertEqual(cep.value, '17500000')
        
    # 2. Testando a formatação 
    def test_format_cep(self):
        cep = Cep('17500000')
        formatted_cep = cep.formatted()
        self.assertEqual(formatted_cep, '17500-000')

    # 3. Testando ceps que estão errados de alguma maneira 
    def test_raise_exception_when_cep_is_wrong_format(self):
        with self.assertRaises(Exception):
            Cep.from_str('aaaaaaaaaaaaa') # Caracteres errados
        with self.assertRaises(Exception):
            Cep.from_str('bbbbbbbbbbbbb') # Caracteres errados
            
    # 4. Testando os ceps que são longos 
    def test_raise_exception_when_is_too_big(self):
        with self.assertRaises(Exception):
            Cep.from_str('111111111')
            
    # 5. Testando os ceps que são curtos 
    def test_raise_exception_when_is_too_small(self):
        with self.assertRaises(Exception):
            Cep.from_str('111111')