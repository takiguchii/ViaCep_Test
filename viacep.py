import aiohttp
from cep import Cep, Address, CepService, CepValidationError 


class ViaCepService(CepService):
    
    async def get_address_by_cep(self, cep: Cep) -> Address:
        async with aiohttp.ClientSession() as session:
            url = f'https://viacep.com.br/ws/{cep.value}/json/'
            
            async with session.get(url) as response:
                cep_payload = await response.json()
        
        if 'erro' in cep_payload and cep_payload['erro']: # testando se o CEP não foi encontrado
            raise CepValidationError(f"CEP '{cep.formatted()}' não encontrado ou inexistente na API ViaCep.")

        return Address( # convertendo os dados para um json 
            street=cep_payload['logradouro'],
            city=cep_payload['localidade'],
            neighborhood=cep_payload['bairro'],
            state=cep_payload['uf'],
        )