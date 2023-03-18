from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Strategy:
    db_name = "ideas"
    def __init__(self, data):
        self.idstrategy = data['idstrategy']
        self.name = data['name']
        self.description = data['description']
        self.id_user = data['id_user']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO strategies (name, description, id_user) VALUES (%(name)s, %(description)s, %(id_user)s);"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM strategies;"
        results = connectToMySQL(cls.db_name).query_db(query)
        clusters = []
        for row in results:
            clusters.append( cls(row))
        return clusters
    
    @classmethod
    def count_strategies(cls):
        query = "select count(*) from strategies;"
        result = connectToMySQL(cls.db_name).query_db(query)
        return result