from falcon import testing
from unittest.mock import patch
from web import app
from viacep import ViaCepService
from cep import Address


class WebAppTestCase(testing.TestCase):
    def setUp(self):
        super(WebAppTestCase, self).setUp()

        # Assume the hypothetical `myapp` package has a
        # function called `create()` to initialize and
        # return a `falcon.App` instance.
        self.app = app


class CepResourceTest(WebAppTestCase):

    def test_get_cep(self):
        expected = {
            "city": "Marília",
            "neighborhood": "Marília",
            "street": "Avenida Carlos Gomes",
            "state": "SP"
        }
        address = Address(**expected)

        with patch.object(ViaCepService, 'get_address_by_cep', return_value=address) as mock_method:
            response = self.simulate_get('/cep/17501000')
            mock_method.assert_called_once()

        self.assertEqual(response.status_code, 200)
        address = response.json
        self.assertDictEqual(expected, address)
