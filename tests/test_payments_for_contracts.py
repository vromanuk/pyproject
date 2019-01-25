from tests import client
from tests.requests.payments_for_contracts_requests import get_payments_for_contract


def test_payments_for_contracts(client):
    rv = get_payments_for_contract(client, 1)

    assert bytes('HB1', encoding='utf-8') in rv.data
