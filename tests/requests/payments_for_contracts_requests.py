def get_payments_for_contract(client, cid):
    return client.get('/contracts/' + str(cid) + '/payments', follow_redirects=True)
