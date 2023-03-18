from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.initiative import Initiative
from flask_app.models.type_users import Type_User
from flask_app.models.cluster import Cluster
from flask_app.models.campaing import Campaign
from flask_app.models.idea import Idea
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        if request.form['password'] == request.form['conf-password']:
            data = dict(request.form)
            data['password'] = bcrypt.generate_password_hash(request.form['password'])
            if User.validate_register(request.form):
                usuario = User.save(data)
                print(usuario)
                session['id'] = usuario.iduser
                session['type_user'] = usuario.type_user
                return redirect('/dashboard')
        else:
            flash('Passwords must be the same!')
    return render_template('register.html')

@app.route('/log-user', methods = ['GET','POST'])
def log_user():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")
        usuario = User.get_by_email(email)
        if usuario is None or not bcrypt.check_password_hash(usuario.password, password):
            flash("Mail/Contraseña incorrecto(s)")
            return redirect('/')
        session["id"] = usuario.iduser
        session['type_user'] = usuario.type_user
        return redirect('/dashboard')
    else:
        return redirect('/')

@app.route('/dashboard') # Jony
def dashboard():
    if session.get('id') == None:
            return redirect('/')
    else:
        print(session)
        user_data = User.get_by_id(session)
        count_initiatives = Initiative.count_initiatives()
        count_campaings = Campaign.count_campaings()
        count_ideas = Idea.count_ideas()
        count_clusters = None
        count_hipexp = None
        count_ideas_by_user = None
        count_comentarios = None
    return render_template("user_dash.html", user_data = user_data, count_initiatives = count_initiatives, count_campaings = count_campaings, count_ideas = count_ideas)

@app.route('/admin/roles') # Jony
def adm_roles():
    if session.get('id') == None:
        return redirect('/')
    elif session.get('type_user') != 1: # esto es para validar rol
        return redirect('/dashboard')
    else:
        print(session)
        user_data = User.get_by_id(session)
        print(user_data)
    return render_template("adm_roles.html", user_data = user_data, tipo_roles = Type_User.get_all(), real_users = User.get_name_lastname_role())

@app.route('/admin/roles-update', methods = ['POST']) # Jony
def update_roles():
    if session.get('id') == None:
            return redirect('/')
    datos_update = {
        "iduser" : request.form['iduser'],
        "idtipo" : request.form['idtipo']
    }
    print(datos_update['iduser'], datos_update['idtipo'])
    User.update_role(datos_update)
    return redirect('/admin/roles')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
    
@app.route('/campaings') # Jony
def view_campaings():
    if session.get('id') == None:
        return redirect('/')
    return render_template('campaings.html')

@app.route('/profile')
def view_profile():
    if session.get('id') == None:
        return redirect('/')
    users= User.get_by_id(session)
    return render_template('profiletrue.html', users= users)


@app.route('/profile/update', methods = ['POST', 'GET'])
def update_profile():
    if session.get('id') == None:
            return redirect('/')
    data = {
        "iduser" : session['id'],
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email']
    }

    User.update_profile(data)
    return redirect('/dashboard')

