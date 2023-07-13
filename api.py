import os
from loggers import init_logger
from flask import Flask, request
# from relogin1 import get_relogin1
# from ack import get_ack
# from json_data import get_json_data
from main import voter_validation_api,captcha_verify,gat_details_api

logger = init_logger("VOTER")

server = os.getenv("SERVER")
port = os.getenv("API_VERSION_PORT")
db = os.getenv("DB")

app = Flask(__name__)

@app.route("/login", methods=["POST", "GET"])
def login_api():
    return voter_validation_api(request)

@app.route("/captcha_verify", methods=["POST", "GET"])
def captcha_verify_api():
    return captcha_verify(request)

@app.route("/get_details", methods=["POST", "GET"])
def details_api():
    return gat_details_api(request)


if __name__ == '__main__':
    app.run(debug=True)