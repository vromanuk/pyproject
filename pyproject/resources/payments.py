from ..services.payments import get_payment_id, get_payments, update_payment, delete_payment, add_new_payment
from flask_restful import Resource
from flask import jsonify, make_response, request
from pyproject.schemas import PaymentsSchema
from marshmallow import ValidationError


class Payment(Resource):
    def get(self, payment_id):
        payment = get_payment_id(payment_id)

        return make_response(jsonify(payment), 200)

    def put(self, payment_id):
        json_data, err = PaymentsSchema(strict=True).load(request.get_json())
        if err:
            raise ValidationError
        payment = update_payment(json_data, payment_id)

        return make_response(jsonify(payment), 201)

    def delete(self, payment_id):
        payment = delete_payment(payment_id)

        return make_response(jsonify(payment), 200)


class Payments(Resource):
    def get(self):
        payments = get_payments()

        return make_response(jsonify(payments), 200)

    def post(self):
        json_data, err = PaymentsSchema(strict=True).load(request.get_json())
        if err:
            raise ValidationError
        payment = add_new_payment(json_data)

        return make_response(jsonify(payment), 201)
