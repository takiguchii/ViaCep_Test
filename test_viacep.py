import aiohttp
from cep import Cep, Address
from viacep import ViaCepService
from aiounittest import AsyncTestCase


class ViaCepServiceTest(AsyncTestCase):
    
    async def test_17519460(self):
        service = ViaCepService()
        cep = Cep.from_str('17519460')
        address = await service.get_address_by_cep(cep)
        self.assertIsInstance(address, Address)
        self.assertEqual(address.street, 'Rua João Tudella')
        self.assertEqual(address.city, 'Marília')
        self.assertEqual(address.neighborhood, 'Jardim Parati')
        self.assertEqual(address.state, 'SP')
    
    async def test_17501000(self):
        service = ViaCepService()
        cep = Cep.from_str('17501000')
        address = await service.get_address_by_cep(cep)
        self.assertIsInstance(address, Address)
        self.assertEqual(address.street, 'Avenida Carlos Gomes')
        self.assertEqual(address.city, 'Marília')
        self.assertEqual(address.neighborhood, 'Marília')
        self.assertEqual(address.state, 'SP')


class ViaCepTest(AsyncTestCase):
    
    async def test_via_cep_api(self):
        expected_payload = {
            "cep": "17519-460",
            "logradouro": "Rua João Tudella",
            "complemento": "",
            "unidade": "",
            "bairro": "Jardim Parati",
            "localidade": "Marília",
            "uf": "SP",
            "estado": "São Paulo",
            "regiao": "Sudeste",
            "ibge": "3529005",
            "gia": "4388",
            "ddd": "14",
            "siafi": "6681"
        }

        async with aiohttp.ClientSession() as session:
            async with session.get('https://viacep.com.br/ws/17519460/json/') as response:
                cep_payload = await response.json()
                self.assertDictEqual(expected_payload, cep_payload)
        