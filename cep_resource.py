from viacep import ViaCepService
from cep import Cep, CepService, CachedCepService
import json
from dataclasses import asdict, dataclass

@dataclass
class CepResource:
    
    cep_service: CepService
    
    async def on_get(self, request, response, cep: str):
        cep = Cep.from_str(cep)
        address = await self.cep_service.get_address_by_cep(cep)
        response.status_code = 200
        response.content_type = 'application/json'
        response.text = json.dumps(asdict(address))