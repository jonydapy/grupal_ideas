from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.initiative import Initiative
from flask_app.models.type_users import Type_User
from flask_app.models.cluster import Cluster
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/initiative/create') # Jony
def initiative():
    if session.get('id') == None:
        return redirect('/')
    if session.get('type_user') == 1 or session.get('type_user') == 4:
        user_data = User.get_by_id(session)
        print(Cluster.get_all())
        return  render_template('create_initiative.html', all_clusters = Cluster.get_all(), user_data = user_data)
    else:
        return redirect('/')
    
@app.route('/initiative/create-now', methods = ['GET','POST']) # Jony
def create_initiative():
    if request.method == 'POST':
        data = dict(request.form)
        Initiative.save(data)
        return redirect('/initiative/create')
    return redirect('/')

@app.route('/initiative/list') # Jony
def list_of_initiatives():
    if session.get('id') == None:
        return redirect('/')
    if session.get('type_user') == 1 or session.get('type_user') == 4:
        user_data = User.get_by_id(session)
        return render_template('initiative_list.html', all_initiatives = Initiative.get_initiative_w_cluster(), user_data = user_data)
    else:
        return redirect('/')


