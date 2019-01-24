from flask_restful import Resource
from flask import jsonify, make_response

from pyproject.services.payments_for_contract import get_payments_for_contract


class PaymentsForContract(Resource):
    def get(self, contract_id):
        contract = get_payments_for_contract(contract_id)

        return make_response(jsonify(contract), 200)
