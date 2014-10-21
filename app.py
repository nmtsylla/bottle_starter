try:
	import gevent.monkey
	gevent.monkey.patch_all()
except:
	pass

import os
from bottle import route, run, Bottle, request, template, get, post

app = Bottle()

@route('/hello')
def hello():
    return "Hello World!"

@get('/test')
def test():
    return template('{{nom}} mesure {{taille}} cm', nom=request.params.nom, taille=request.params.taille)

@post('/signup')
def signup():
    return template('username={{nom}} email={{email}}', nom=request.params.username, email=request.params.email)


run(server='gevent', host='0.0.0.0', port='8090')