from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.idea import Idea
from flask_app.models.initiative import Initiative
from flask_app.models.type_users import Type_User
from flask_app.models.comentario import Comment

#from flask_app.models.agendamiento import Agendamiento
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/verideas/<int:id_campaign>')
def verideadecampaign(id_campaign):
    data = {
        "id_campaign": id_campaign
    }
    return render_template('ideas.html', ideas=Idea.get_allideasporusuario(data))

@app.route('/verideaporid/<int:ididea>')
def commentidea(ididea):
    data = {
        "ididea": ididea
    }
    comments= Comment.get_allcommentsporidea(data)
    return render_template('comments.html', ideas=Idea.get_by_ididea(data), comments=comments)


@app.route('/savecomment/<int:ididea>',methods=['post'])
def savecomment(ididea):
    # if session.get('id') == None:
    #        return redirect('/')
    #else:
        data={
            "comment":request.form['comment'],
            "id": session["id"],
            "ididea": ididea
        }
        Comment.savecomment(data)
        comments= Comment.get_allcommentsporidea(data)
        return render_template('comments.html', ideas=Idea.get_by_ididea(data), comments=comments)
