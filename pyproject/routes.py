from pyproject.resources.smoke import Smoke
from pyproject.resources.contracts import Contracts, Contract
from pyproject.resources.payments import Payments, Payment
from pyproject import api

api.add_resource(Smoke, '/smoke')

api.add_resource(Contracts, '/contracts', strict_slashes=False)
api.add_resource(Contract, '/contracts/<int:contract_id>', strict_slashes=False)

api.add_resource(Payments, '/payments', strict_slashes=False)
api.add_resource(Payment, '/payments/<int:payment_id>', strict_slashes=False)
