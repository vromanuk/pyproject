import json

from tests import client
from tests.requests.payments_requests import get_all_payments, get_particular_payment, add_payment, change_payment, \
    delete_payment
from tests.requests.contracts_requests import get_all_contracts, delete_contract


def test_get_all_payments(client):
    rv = get_all_payments(client)
    assert bytes('15', encoding='utf-8') in rv.data


def test_get_particular_payment(client):
    rv = get_all_payments(client)
    rs = json.loads(rv.data, encoding='utf-8')

    cid = rs[0].get('id')
    rv = get_particular_payment(client, cid)

    assert bytes('15', encoding='utf-8') in rv.data


def test_nonexistent_id(client):
    cid = pow(2, 16)
    rv = get_particular_payment(client, cid)

    assert bytes('Such id does not exist', encoding='utf-8') in rv.data


def test_add_payment(client):
    rv = get_all_contracts(client)
    rs = json.loads(rv.data, encoding='utf-8')

    cid = rs[-1].get('id')
    rv = add_payment(client, cid, 10)
    assert bytes('Created successfully', encoding='utf-8') in rv.data


def test_change_payment(client):
    rv = get_all_contracts(client)
    rs = json.loads(rv.data, encoding='utf-8')

    cid = rs[-1].get('id')
    rv = change_payment(client, cid, 25)
    assert bytes('25', encoding='utf-8') in rv.data


def test_delete_payment(client):
    rv = get_all_contracts(client)
    rs = json.loads(rv.data, encoding='utf-8')

    cid = rs[-1].get('id')
    rv = delete_payment(client, cid)

    assert bytes(f'Payment {cid} deleted successfully', encoding='utf-8') in rv.data


def test_delete_contract(client):
    rv = get_all_contracts(client)
    rs = json.loads(rv.data, encoding='utf-8')

    cid = rs[-1].get('id')
    rv = delete_contract(client, cid)

    assert bytes(f'Contract {cid} deleted successfully', encoding='utf-8') in rv.data
