from pyproject import api
from pyproject.resources.smoke import Smoke
from pyproject.resources.payments import PaymentsResource
from pyproject.resources.contracts import ContractsResource
from pyproject.resources.payments_for_contract import PaymentsForContract

api.add_resource(Smoke, '/smoke')

api.add_resource(ContractsResource, '/contracts', '/contracts/<int:contract_id>', strict_slashes=False)
api.add_resource(PaymentsResource, '/payments', '/payments/<int:payment_id>', strict_slashes=False)

api.add_resource(PaymentsForContract, '/contracts/<int:contract_id>/payments', strict_slashes=False)
