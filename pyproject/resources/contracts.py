from ..services.contracts import get_contract_id, get_contracts, update_contract, delete_contract, add_new_contract
from flask_restful import Resource
from flask import jsonify, make_response


class Contract(Resource):
    def get(self, contract_id):
        contract = get_contract_id(contract_id)

        return make_response(jsonify(contract), 200)

    def put(self, data, contract_id):
        contract = update_contract(data, contract_id)

        return make_response(jsonify(contract), 201)

    def delete(self, contract_id):
        contract = delete_contract(contract_id)

        return make_response(jsonify(contract), 200)


class Contracts(Resource):
    def get(self):
        contracts = get_contracts()

        return make_response(jsonify(contracts), 200)

    def post(self, json_data):
        contract = add_new_contract(json_data)
        return make_response(jsonify(contract), 201)
