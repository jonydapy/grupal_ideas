from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.initiative import Initiative
from flask_app.models.idea import Idea
from flask_app.models.cluster import Cluster
from flask_app.models.hipexp import Hip_Exp
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/hypothesis') # Jony
def hypothesis():
    if session.get('id') == None:
        return redirect('/')
    if session.get('type_user') == 1 or session.get('type_user') == 4:
        user_data = User.get_by_id(session)
        return  render_template('hip_and_exp.html', all_initiatives = Initiative.get_all(), user_data = user_data)
    else:
        return redirect('/')
    
@app.route('/hypothesis/see/<int:id_ini>') # Jony
def see_hypothesis(id_ini):
    if session.get('id') == None:
        return redirect('/')
    if session.get('type_user') == 1 or session.get('type_user') == 4:
        user_data = User.get_by_id(session)
        data = {
            "id_initiative" : id_ini
        }
        return  render_template('hyp_in_initiative.html', hip_exp = Hip_Exp.get_by_initiative(data), user_data = user_data, initiative_name = Initiative.get_by_id(data))
    else:
        return redirect('/')

