from flask_moment import Moment
from flask import Flask,render_template,session ,redirect,url_for,flash
from datetime import datetime
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField , SubmitField
from wtforms.validators import Required


class NameForm(Form):
	name = StringField('hello ,your name?',validators=[Required()])
	submit = SubmitField('Submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ni cai bu dao de'
moment = Moment(app)
bootstrap = Bootstrap(app)

@app.route("/",methods=['GET','POST'])
def index(): 
	#name = None
	form = NameForm()
	if form.validate_on_submit():
		#name = form.name.data
		old_name = session.get("name")
		if old_name is not None and old_name != form.name.data:
			flash('ni shu de shi shen me gui dongxi ?')
			flash('aaaaaaaaaaaaaaaa')
		session['name'] = form.name.data
		return redirect(url_for('index'))
	return render_template('index.html', form = form , name = session.get('name') ,current_time = datetime.utcnow())

@app.route('/home')
def home():
	return render_template('404.html')

@app.route('/login')
def logian():
	return render_template("500.html")


if __name__ == "__main__":
	app.run(host="0.0.0.0")


