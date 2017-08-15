from flask import Flask,render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
	name='nanshao'
	return render_template('hello.html',name=name)

@app.route("/home")
def errorla():
	return render_template('500.html')

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html',404)

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html',500)


if __name__ == '__main__':
	manager.run()

