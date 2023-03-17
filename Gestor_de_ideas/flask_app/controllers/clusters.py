from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.initiative import Initiative
from flask_app.models.idea import Idea
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
    
@app.route('/cluster/create-now', methods = ['GET','POST']) # Jony
def create_cluster():
    if request.method == 'POST':
        data = dict(request.form)
        Cluster.save(data)
        return redirect('/cluster/create')
    return redirect('/')

@app.route('/cluster/ideas/<int:cluster>') # Jony
def initiative_in_cluster(cluster):
    if session.get('id') == None:
        return redirect('/')
    if session.get('type_user') == 1 or session.get('type_user') == 4:
        user_data = User.get_by_id(session)
        data = {
            "id_cluster": cluster
        }
        all_ideas = Cluster.get_ideas_in_cluster(data)
        print(len(all_ideas))
        if len(all_ideas) < 1:
            flash("This cluster is Empty - Please choose another Cluster")
            return redirect('/cluster/create')
        return  render_template('initiatives_in_cluster.html', user_data = user_data, all_ideas = all_ideas)
    else:
        return redirect('/')

@app.route('/cluster/ideas') # Jony
def cluster_ideas():
    if session.get('id') == None:
        return redirect('/')
    if session.get('type_user') == 1 or session.get('type_user') == 4:
        user_data = User.get_by_id(session)
        return  render_template('cluster_ideas.html', ideas = Cluster.get_ideas_to_cluster(), user_data = user_data, clusters = Cluster.get_all())
    else:
        return redirect('/')

    
@app.route('/cluster/ideas/cluster-this', methods = ['GET', 'POST']) # Jony
def cluster_this():
    if request.method == 'POST':
        data = {
            "idcluster" : request.form['idcluster'],
            "ididea" : request.form['ididea']
        }
        Idea.update_cluster(data)
        return redirect('/cluster/ideas')
    return redirect('/')