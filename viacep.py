import aiohttp
from cep import Cep, Address, CepService

class ViaCepService(CepService):
    

    async def get_address_by_cep(self, cep: Cep) -> Address:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://viacep.com.br/ws/{cep.value}/json/') as response:
                cep_payload = await response.json()
                
        return Address(
            street=cep_payload['logradouro'],
            city=cep_payload['localidade'],
            neighborhood=cep_payload['bairro'],
            state=cep_payload['uf'],
        )