from flask_app import app
from flask_app.controllers import users,ideas, campaings, initiatives, clusters
if __name__=="__main__":
    app.run(debug=True)