from marshmallow import Schema, fields


class ContractsSchema(Schema):
    title = fields.String(required=True)
    price = fields.Float(required=True)
    description = fields.String()


class PaymentsSchema(Schema):
    contracts_id = fields.Integer(required=True)
    amount = fields.Float(required=True)
