def success(data, res, code=200):
    data['status'] = 'success'
    return res(data), code
