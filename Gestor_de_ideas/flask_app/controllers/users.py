from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.user import User
#from flask_app.models.initiative import Initiative
#from flask_app.models.agendamiento import Agendamiento
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

    """ if not User.validate_register(request.form):
        return redirect('/')
    data ={ 
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(data)
    session['user_id'] = id
    return redirect('/dashboard') """

@app.route('/log-user', methods = ['GET','POST'])
def log_user():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")
        usuario = User.get_by_email(email)
        if usuario is None or not bcrypt.check_password_hash(usuario.user_password, password):
            flash("Mail/Contraseña incorrecto(s)")
            return redirect('/')
        session["id"] = usuario.id_user
        print(session, "***checkeo exitoso***")
        return redirect('/home')
    else:
        return redirect('/')
    
    """ user = User.get_by_email(request.form)
    if not user:
        flash("Invalid Email","login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password","login")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/dashboard') """

@app.route('/dashboard')
def dashboard():
    if session.get('id') == None:
            return redirect('/')
    else:
        print(session)
        user_data = User.get_by_id(session)
        print(user_data)
    return render_template("user_dash.html", user_data = user_data)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/create/initiative') # Jony
def initiative():
    if session.get('user_id') == None:
        return redirect('/login')
    if session.get('type_user') == "Admin" or session.get('type_user') == "Lider":
        return  render_template('give_initiatives.html')
    else:
        return redirect('/login')