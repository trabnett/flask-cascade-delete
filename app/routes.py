from flask import render_template, request
from app import app
from app.forms import LoginForm

@app.route('/', methods=['GET', 'POST'])
def welcome():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        return "yes"

    return render_template('welcome.html', form=form)