from .resources.smoke import Smoke
from .resources.contracts import Contracts, Contract
from pyproject import api

api.add_resource(Smoke, '/smoke')
api.add_resource(Contract, '/contracts/<int:contract_id>', strict_slashes=False)
api.add_resource(Contracts, '/contracts', strict_slashes=False)
