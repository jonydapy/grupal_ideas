from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.initiative import Initiative
from flask_app.models.strategy import Strategy
from flask_app.models.cluster import Cluster
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/strategies/create') # Jony
def strategie():
    if session.get('id') == None:
        return redirect('/')
    if session.get('type_user') == 1 or session.get('type_user') == 2:
        user_data = User.get_by_id(session)
        return  render_template('create_strategie.html', all_strategies = Strategy.get_all(), user_data = user_data)
    else:
        return redirect('/')

@app.route('/strategies/create-now', methods = ['GET','POST']) # Jony
def create_strategy():
    if request.method == 'POST':
        data = dict(request.form)
        Strategy.save(data)
        return redirect('/strategies/create')
    return redirect('/')

