from flask import Flask, Response, request
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from flask_cors import CORS
import argparse
import base64

from read_stream import get_stream

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key here'
authBasic = HTTPBasicAuth()
authToken = HTTPTokenAuth(scheme='Bearer')
cors = CORS(app, resources={r"/*": {"origins": "*"}})

users = {
    "admin": "admin",  # Basic YWRtaW46YWRtaW4=
}

tokens = {
    "admin": "admin"  # Bearer admin
}


@authBasic.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None


@authToken.verify_token
def verify_token(token):
    if token in tokens:
        return tokens[token]


@app.route('/')
def index():
    return "server online"


@app.route('/basicStream')
@authBasic.login_required
def http_basic_stream():
    # /basicStream?url=<base64 url>
    userInput = request.args.get('url')
    if userInput == None:
        return Response(get_stream(0),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
    url = base64.b64decode(userInput).decode('utf-8')
    if not url.strip():
        return Response('Missing parameters, eg. /stream?url=base64 url', status=400)

    return Response(get_stream(url),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/tokenStream')
@authToken.login_required
def http_token_stream():
    # /tokenStream?url=<base64 url>
    userInput = request.args.get('url')
    if userInput == None:
        return Response(get_stream(0),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
    url = base64.b64decode(userInput).decode('utf-8')
    if not url.strip():
        return Response('Missing parameters, eg. /stream?url=base64 url', status=400)

    return Response(get_stream(url),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/stream')
def http_stream():
    # /stream?url=<base64 url>
    userInput = request.args.get('url')
    if userInput == None:
        return Response(get_stream(0),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
    url = base64.b64decode(userInput).decode('utf-8')
    if not url.strip():
        return Response('Missing parameters, eg. /stream?url=base64 url', status=400)

    return Response(get_stream(url),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Video Server")
    parser.add_argument("--port",
                        type=int,
                        default=5000,
                        help="Running on the given port")
    args: argparse.Namespace = parser.parse_args()
    app.run(host='0.0.0.0', debug=True, port=args.port)
