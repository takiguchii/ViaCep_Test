import aiohttp
from cep import Cep, Address
from viacep import ViaCepService
from aiounittest import AsyncTestCase


class ViaCepServiceTest(AsyncTestCase):
    
    async def test_17672050(self):
        service = ViaCepService()
        cep = Cep.from_str('17672050')
        address = await service.get_address_by_cep(cep)
        self.assertIsInstance(address, Address)
        self.assertEqual(address.street, 'Rua Principal')
        self.assertEqual(address.city, 'Quintana')
        self.assertEqual(address.neighborhood, 'Centro')
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
            "cep": "17672-050",
            "logradouro": "Rua Principal",
            "complemento": "",
            "unidade": "",
            "bairro": "Centro",
            "localidade": "Quintana",
            "uf": "SP",
            "estado": "São Paulo",
            "regiao": "Sudeste",
            "ibge": "3541204",
            "gia": "",
            "ddd": "14",
            "siafi": "6685"
        }

        async with aiohttp.ClientSession() as session:
            async with session.get('https://viacep.com.br/ws/17672050/json/') as response:
                cep_payload = await response.json()
                self.assertDictEqual(expected_payload, cep_payload)
