def is_json(req, res, next):
    if not req.json:
        return res({"status": "Error: Invalid JSON"}), 400
    return next()

def internal_server_error(res, message):
    return res({"status": "Internal Server Error: " + message}), 500
