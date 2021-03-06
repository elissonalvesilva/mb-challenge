from config.settings import Settings
from flask import Flask, request, jsonify

from api.main.factories.controllers.get_mms_controller_factory import make_mms_controller
from api.presentation.protocols.request import Request

app = Flask(__name__)

@app.route('/<pair>/mms', methods=['GET'])
def get_mms(pair):
    args = request.args
    controller = make_mms_controller()
    req = Request(pair, args)
    response = controller.handler(req)

    if response.status_code >= 400:
        return jsonify({ 'error': response.body.message }), response.status_code

    return jsonify(response.body), response.status_code


if __name__ == "__main__":
    app.run(host=Settings.API_HOST, port=int(Settings.API_PORT))
