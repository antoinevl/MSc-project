from bottle import route, run, template
from base64 import b64encode, b64decode

@route('/prediction/<urlb64>')
def predict(urlb64):
	url = b64decode(urlb64)
	return "URL: "+url+"."

run(host='146.169.47.251', port=8080)
