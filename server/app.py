from flask import Flask, request, jsonify
from flask_cors import CORS
from server.middleware.middleware import pipe
from server.middleware.errors import is_json, internal_server_error
from server.controllers.option.option import get_option_price_data
from server.controllers.stock.stock import get_stock_data

app = Flask(__name__)
CORS(app)

@app.route('/api', methods=['POST'])
def stock_endpoint():
    try:
        return pipe(
            request,
            jsonify,
            is_json,
            get_stock_data
        )
    except Exception as e:
        return internal_server_error(jsonify, str(e))
 
@app.route('/api/options', methods=['POST'])
def option_endpoint():
    try: 
        return pipe(
            request,
            jsonify,
            is_json,
            get_option_price_data
        )
    except Exception as e:
        return internal_server_error(jsonify, str(e))

if __name__ == "__main__":
    app.run(debug=True)
