import json

from tests import client
from tests.requests.contracts_requests import get_all_contracts, get_particular_contract, add_contract, change_contract


def test_get_all_contracts(client):
    rv = get_all_contracts(client)
    assert bytes('HB1', encoding='utf-8') in rv.data


def test_get_particular_contract(client):
    rv = get_all_contracts(client)
    rs = json.loads(rv.data, encoding='utf-8')

    cid = rs[0].get('id')
    rv = get_particular_contract(client, cid)

    assert bytes('HB1', encoding='utf-8') in rv.data


def test_nonexistent_id(client):
    cid = pow(2, 16)
    rv = get_particular_contract(client, cid)

    assert bytes('Such id does not exist', encoding='utf-8') in rv.data


def test_add_contract(client):
    rv = add_contract(client, "HCL", 13.99,
                      "Tramadol is used to help relieve moderate to moderately severe pain. Is similar to opiod.")
    assert bytes('Created successfully', encoding='utf-8') in rv.data


def test_change_contract(client):
    rv = get_all_contracts(client)
    rs = json.loads(rv.data, encoding='utf-8')

    cid = rs[-1].get('id')
    rv = change_contract(client, cid, 19.99)
    assert bytes('19.99', encoding='utf-8') in rv.data
