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
    if session.get('id') == None:
        return redirect('/')
    data = {
        "id_campaign": id_campaign
    }
    if len(Idea.get_allideasporusuario(data)) != 0:
        ideas=Idea.get_allideasporusuario(data)
    else:
        ideas = [{
            "ididea": "",
            "content": "There is no ideas here, please add one",
            "first_name":"",
            "last_name":"",
            "id_campaign": id_campaign
        }]
    return render_template('ideas.html', ideas=ideas)

@app.route('/verideas/guardar', methods = ['GET','POST']) # Jony
def save_idea():
    if request.method == 'POST':
        if session.get('id') == None:
            return redirect('/')
        data={
            "content":request.form['content'],
            "id": session["id"],
            "id_campaign": request.form['id_campaign']
        }
        pagina = request.form['id_campaign']
        Idea.save(data)
        return redirect('/verideas/{}'.format(pagina))
    return redirect('/')


@app.route('/verideaporid/<int:ididea>')
def commentidea(ididea):
    if session.get('id') == None:
        return redirect('/')
    data = {
        "ididea": ididea
    }
    comments= Comment.get_allcommentsporidea(data)
    return render_template('comments.html', ideas=Idea.get_by_ididea(data), comments=comments)


@app.route('/savecomment/<int:ididea>',methods=['post'])
def savecomment(ididea):
        if session.get('id') == None:
            return redirect('/')
        data={
            "comment":request.form['comment'],
            "id": session["id"],
            "ididea": ididea
        }
        Comment.savecomment(data)
        comments= Comment.get_allcommentsporidea(data)
        return render_template('comments.html', ideas=Idea.get_by_ididea(data), comments=comments)
        

@app.route('/saveidea',methods=['post'])
def save():
    # if session.get('id') == None:
    #        return redirect('/')
    #else:
        data={
            "content":request.form['content'],
            "id": session["id"],
            "id_campaign": session['id_campaign']
        }
        datab={
            "id_campaign": session['id_campaign']
        }
        Idea.save(data)
        #return render_template('ideas.html', ideas=Idea.get_allideasporusuario(datab))
        return redirect("/verideas/", ididea = session['id_campaign'])