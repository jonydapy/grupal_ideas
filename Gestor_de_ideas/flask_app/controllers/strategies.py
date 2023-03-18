from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.initiative import Initiative
from flask_app.models.type_users import Type_User
from flask_app.models.cluster import Cluster
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/strategies/create') # Jony
def strategie():
    if session.get('id') == None:
        return redirect('/')
    if session.get('type_user') == 1 or session.get('type_user') == 2:
        user_data = User.get_by_id(session)
        return  render_template('create_strategie.html', all_clusters = Cluster.get_all(), user_data = user_data)
    else:
        return redirect('/')
    


