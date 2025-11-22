from dataclasses import dataclass

"""
Dataclasse = ele incurta a criação das classes definindo apenas os atributoos que são os mais importantes
Frozen = deixa o arquivo imutável
"""
@dataclass(frozen=True)
class Cep:
    value: str

    def formatted(self) -> str:
        """Retorna o CEP formatado como 'XXXXX-XXX'."""
        # Exemplo: '17500000' -> '17500-000'
        return self.value[:5] + '-' + self.value[5:]


# 2. Classe de Dados Simples para o Endereço
# Representa a resposta padronizada da API, com todos os campos essenciais.

@dataclass
class Address:
    city: str
    neighborhood: str
    street: str
    state: str
