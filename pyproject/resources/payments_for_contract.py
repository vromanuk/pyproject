from flask_restful import Resource

from pyproject.services.payments_for_contract import get_payments_for_contract


class PaymentsForContract(Resource):
    def get(self, contract_id):
        contract = get_payments_for_contract(contract_id)

        return contract, 200
