from flask_app import app
from flask_app.controllers import users,ideas, campaings, initiatives, clusters, hipexps
if __name__=="__main__":
    app.run(debug=True)