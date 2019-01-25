def get_all_payments(client):
    return client.get('/payments', follow_redirects=True)


def get_particular_payment(client, cid):
    return client.get('/payments/' + str(cid), follow_redirects=True)


def add_payment(client, cid, amount):
    return client.post('/payments/', json=dict(
        contracts_id=cid,
        amount=amount
    ), follow_redirects=True)


def change_payment(client, cid, amount=42):
    return client.put('/payments/' + str(cid), json=dict(
        contracts_id=cid,
        amount=amount
    ), follow_redirects=True)


def delete_payment(client, cid):
    return client.delete('/payments/' + str(cid), follow_redirects=True)
