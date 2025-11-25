from abc import ABC, abstractmethod
from typing import Awaitable
from dataclasses import dataclass

"""
Dataclasse = ele incurta a criação das classes definindo apenas os atributoos que são os mais importantes
Frozen = deixa o arquivo imutável
"""
@dataclass(frozen=True)
class Cep:
    value: str

    def formatted(self) -> str:
        return self.value[:5] + '-' + self.value[5:]; "Retornando o valor formatado do cep"

@dataclass
class Address:
    city: str
    neighborhood: str
    street: str
    state: str
    
"@abstractmethod definindo que é uma classe abstrata"
class CepService(ABC):
    @abstractmethod 
    async def get_address_by_cep(self, cep: Cep) -> Awaitable[Address]:
        raise NotImplementedError()