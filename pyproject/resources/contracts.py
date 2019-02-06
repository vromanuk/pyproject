from flask_restful import Resource
from pyproject.schemas import ContractsSchema
from flask import request
from pyproject.services.base_service import contract_


class ContractsResource(Resource):
    def get(self, contract_id=None):
        if not contract_id:
            contracts = contract_.get_resources()
            return contracts, 200

        contract = contract_.get_resource(contract_id)

        return contract, 200

    def post(self):
        json_data, errors = ContractsSchema().load(request.json)
        if errors:
            return errors, 422
        contract = contract_.add_new_resource(json_data)

        return contract, 201

    def put(self, contract_id):
        json_data, errors = ContractsSchema().load(request.json)
        if errors:
            return errors, 422
        contract = contract_.update_resource(json_data, contract_id)

        return contract, 201

    def delete(self, contract_id):
        contract = contract_.delete_resource(contract_id)

        return contract, 200
