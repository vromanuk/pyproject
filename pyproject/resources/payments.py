from flask_restful import Resource
from pyproject.schemas import PaymentsSchema
from flask import request
from pyproject.services.base_service import payment_


class PaymentsResource(Resource):
    def get(self, payment_id=None):
        if not payment_id:
            payments = payment_.get_resources()
            return payments, 200

        payment = payment_.get_resource_id(payment_id)

        return payment, 200

    def post(self):
        json_data, errors = PaymentsSchema().load(request.json)
        if errors:
            return errors, 422
        payment = payment_.add_new_resource(json_data)

        return payment, 201

    def put(self, payment_id):
        json_data, errors = PaymentsSchema().load(request.json)
        if errors:
            return errors, 422
        payment = payment_.update_resource(json_data, payment_id)

        return payment, 201

    def delete(self, payment_id):
        payment = payment_.delete_resource(payment_id)

        return payment, 200
