from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.idea import Idea
from flask_app.models.campaing import Campaign
from flask_app.models.initiative import Initiative
from flask_app.models.type_users import Type_User
from flask_app.models.strategy import Strategy
#from flask_app.models.agendamiento import Agendamiento
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/vercampaigns')
def vercampaigns():
    if session.get('id') == None:
        return redirect('/')
    campaigns = Campaign.get_allcampaing()
    user_data = User.get_by_id(session)
    strategys = Strategy.get_all()
    print(campaigns)
    return render_template('campaings.html', campaigns=campaigns, user_data=user_data, strategys=strategys)

@app.route('/campaign/guardar', methods = ['GET','POST']) # Joel
def save_campaing():
    if request.method == 'POST':
        if session.get('id') == None:
            return redirect('/')
        data={
            "campaign":request.form['content'],
            "idstrategy":request.form['idstrategy']
        }
        Campaign.save(data)
        return redirect('/vercampaigns')
    return redirect('/')