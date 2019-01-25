from tests import client


def test_smoke(client):
    rv = client.get('/smoke')

    assert b'OK' in rv.data
