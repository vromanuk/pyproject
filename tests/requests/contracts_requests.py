def get_all_contracts(client):
    return client.get('/contracts', follow_redirects=True)


def get_particular_contract(client, cid):
    return client.get('/contracts/' + str(cid), follow_redirects=True)


def add_contract(client, title, price, description):
    return client.post('/contracts', json=dict(
        title=title,
        price=price,
        description=description
    ), follow_redirects=True)


def change_contract(client, cid, price, title='default', description='default'):
    return client.put('/contracts/' + str(cid), json=dict(
        price=price,
        title=title,
        description=description
    ), follow_redirects=True)


def delete_contract(client, cid):
    return client.delete('/contracts/' + str(cid), follow_redirects=True)
