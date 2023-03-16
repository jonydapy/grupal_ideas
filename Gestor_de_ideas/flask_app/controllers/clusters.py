from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.initiative import Initiative
from flask_app.models.cluster import Cluster
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/cluster/create') # Jony
def cluster():
    if session.get('id') == None:
        return redirect('/')
    if session.get('type_user') == 1 or session.get('type_user') == 4:
        user_data = User.get_by_id(session)
        return  render_template('create_cluster.html', all_clusters = Cluster.get_all(), user_data = user_data)
    else:
        return redirect('/')



