from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.idea import Idea
from flask_app.models.initiative import Initiative
from flask_app.models.type_users import Type_User
#from flask_app.models.agendamiento import Agendamiento
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/verideaporid/<int:ididea>')
def commentidea(ididea):
    data = {
        "ididea": ididea
    }
    return render_template('comments.html', ideas=Idea.get_by_ididea(data))

@app.route('/savecomment/<int:ididea>')
def savecomment(ididea):
    if session.get('user_id') == None:
            return redirect('/')
    else:
        data={
            "comment":request.form['comment'],
            "user_id": session["user_id"],
            "ididea": ididea
        }
        Idea.save_comment(data)
    return redirect ("comments.html")
