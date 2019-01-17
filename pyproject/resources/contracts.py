from ..services.contracts import get_contract_id, get_contracts, put_contract, delete_contract
from flask_restful import Resource
from flask import make_response


class Contract(Resource):
    def get(self, contract_id):
        contract = get_contract_id(contract_id)
        return {'Title': contract.get('title'), 'Price': contract.get('price'),
                'Description': contract.get('description')}

    def put(self, data, contract_id):
        contract = put_contract(data, contract_id)
        return make_response(contract), 201

    def delete(self, contract_id):
        contract = delete_contract(contract_id)
        return make_response(contract), 200


class Contracts(Resource):
    def get(self):
        contracts = get_contracts()
        return make_response(contracts)
