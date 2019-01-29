from flask_restful import Resource
from pyproject.schemas import PaymentsSchema
from flask import request
from pyproject.services.payments import get_payment_id, get_payments, update_payment, delete_payment, add_new_payment


class Payment(Resource):
    def get(self, payment_id):
        payment = get_payment_id(payment_id)

        return payment, 200

    def put(self, payment_id):
        json_data, errors = PaymentsSchema().load(request.json)
        if errors:
            return errors, 422
        payment = update_payment(json_data, payment_id)

        return payment, 201

    def delete(self, payment_id):
        payment = delete_payment(payment_id)

        return payment, 200


class Payments(Resource):
    def get(self):
        payments = get_payments()

        return payments, 200

    def post(self):
        json_data, errors = PaymentsSchema().load(request.json)
        if errors:
            return errors, 422
        payment = add_new_payment(json_data)

        return payment, 201
