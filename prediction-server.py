from bottle import route, run, template, request, response
from base64 import b64encode, b64decode
from detector import predict
import bottle

def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        # set CORS headers
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

        if bottle.request.method != 'OPTIONS':
            # actual request; reply with the actual response
            return fn(*args, **kwargs)

    return _enable_cors

@route('/prediction')
@enable_cors
def f():
        url = request.query.url
        return "URL: "+url+"<br>Prediction:"+predict(url)+"."

run(host='146.169.47.251', port=8080)