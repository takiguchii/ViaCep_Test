from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Awaitable
import re

CEP_PATTERN = re.compile(r'^\d{5}\-?\d{3}$')

"""
Dataclasse = ele incurta a criação das classes definindo apenas os atributoos que são os mais importantes
Frozen = deixa o arquivo imutável
"""

@dataclass(frozen=True)
class Cep:
    # O valor será sempre armazenado limpo (8 dígitos), garantindo imutabilidade.
    value: str

    @classmethod    
    def from_str(cls, cep_str: str): 
        match = CEP_PATTERN.match(cep_str)
        if not match:
            raise Exception("CEP com formato inválido.")
            
        clean_cep = cep_str.replace('-', '')
        
        return cls(clean_cep)
    
    def formatted(self) -> str:
        """Retorna o CEP formatado como 'XXXXX-XXX'."""
        return self.value[:5] + '-' + self.value[5:]


@dataclass #o dataclass cuida do __init__
class Address:
    city: str
    neighborhood: str
    street: str
    state: str


"@abstractmethod definindo que é uma classe abstrata"
class CepService(ABC):

    @abstractmethod
    async def get_address_by_cep(self, cep: Cep) -> Awaitable[Address]:
        """
        Contrato: Recebe um Cep e promete (Awaitable) retornar um Address.
        """
        raise NotImplementedError()