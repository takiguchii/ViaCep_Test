from dataclasses import dataclass, field
from typing import Dict
from abc import ABC, abstractmethod
import re



CEP_PATTERN = re.compile(r'^\d{5}\-?\d{3}$')

@dataclass
class Cep:
    value: str

    @classmethod    
    def from_str(cls, cep_str: str): 
        match = CEP_PATTERN.match(cep_str)
        if not match:
            raise Exception()
        clean_cep = cep_str.replace('-', '')
        return cls(clean_cep)
    
    def formatted(self) -> str:
        return self.value[:5] + '-' + self.value[5:]
    
@dataclass
class Address:
    city: str = None
    neighborhood: str = None
    street: str = None
    state: str = None
    
class CepService(ABC):
    
    @abstractmethod
    async def get_address_by_cep(self, cep: Cep) -> Address:
        raise NotImplementedError()
                
# decorator
@dataclass      
class CachedCepService(CepService):
    
    cep_service: CepService
    cache: Dict[str, Address] = field(default_factory=dict)
    
    async def get_address_by_cep(self, cep: Cep) -> Address:
        if cep.value in self.cache:
            print("from cache")
            return self.cache[cep.value]
        address = await self.cep_service.get_address_by_cep(cep)
        self.cache[cep.value] = address
        print("from service")
        return address