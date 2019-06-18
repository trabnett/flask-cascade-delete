from flask import render_template, request, redirect
from app import app
from app import db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.forms import UserForm, OptionsForm
from app.models import User, Option, UserOption

engine = db.engine
Session = sessionmaker(engine)
session = Session()

@app.route('/', methods=['GET', 'POST'])
def welcome():
    form = UserForm()
    if request.method == 'POST' and form.validate():
        x = User(name=request.form.get('name'),level=request.form.get('level'))
        db.session.add(x)
        db.session.commit()
        return redirect('/')
    users = User.query.all()
    return render_template('welcome.html', form=form, users=users)

@app.route('/options', methods=['GET', 'POST'])
def options():
    form = OptionsForm()
    if request.method == 'POST' and form.validate():
        x = Option(option=request.form.get('option'),level=request.form.get('level'))
        db.session.add(x)
        db.session.commit()
        return redirect('/options')
    options = Option.query.all()
    return render_template('options.html', form=form, options=options)

@app.route('/user/options', methods=['Post'])
def create_user_option():
    if request.method == 'POST':
        x = request.form
        for y in x:
            z = UserOption(user_id=x[y], option_id=y)
            db.session.add(z)
            db.session.commit()
            print(y, x[y])
            return redirect(f'/user/{x[y]}')
    return "no"

@app.route('/user/<int:id>')
def user(id):
    options = session.query(User, Option, UserOption).filter(User.id == UserOption.user_id
    ).filter(Option.id == UserOption.id).all()
    print(options[0][0])
    return render_template('user.html', id=id, options=options)

@app.route('/options/<int:id>/delete', methods=['POST'])
def delete(id):
    user_id = 0
    for y in request.form:
        user_id = y
        print(y, request.form[y])
        uo = Option.query.filter_by(id=request.form[y]).first()
        session.delete(uo)
        session.commit()
    return redirect (f'/user/{user_id}')