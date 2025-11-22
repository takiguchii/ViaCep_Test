import falcon.asgi
from cep_resource import CepResource
from cep import CachedCepService
from viacep import ViaCepService

cep_service = CachedCepService(
    ViaCepService()
)

app = falcon.asgi.App()

app.add_route('/cep/{cep}', CepResource(cep_service))
