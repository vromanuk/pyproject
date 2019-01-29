from flask_restful import Resource
from pyproject.schemas import ContractsSchema
from flask import request
from pyproject.services.contracts import get_contract_id, get_contracts, update_contract, delete_contract, \
    add_new_contract


class Contract(Resource):
    def get(self, contract_id):
        contract = get_contract_id(contract_id)

        return contract, 200

    def put(self, contract_id):
        json_data, errors = ContractsSchema().load(request.json)
        if errors:
            return errors, 422
        contract = update_contract(json_data, contract_id)

        return contract, 201

    def delete(self, contract_id):
        contract = delete_contract(contract_id)

        return contract, 200


class Contracts(Resource):
    def get(self):
        contracts = get_contracts()

        return contracts, 200

    def post(self):
        json_data, errors = ContractsSchema().load(request.json)
        if errors:
            return errors, 422
        contract = add_new_contract(json_data)

        return contract, 201
