from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.idea import Idea
from flask_app.models.campaing import Campaign
from flask_app.models.initiative import Initiative
from flask_app.models.type_users import Type_User
#from flask_app.models.agendamiento import Agendamiento
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/vercampaigns')
def vercampaigns():
    return render_template('campaings.html', campaings= Campaign.get_allcampaing())