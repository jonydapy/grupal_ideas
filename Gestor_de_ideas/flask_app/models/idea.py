from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Idea:
    db_name = "ideas"
    def __init__(self,data):
        self.ididea = data['ididea']
        self.content = data['content']
        self.user_id = data['user_id']
        self.id_cluster = data['id_cluster']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO ideas (content, user_id, id_cluster) VALUES (%(content)s,%(user_id)s,%(id_cluster)s);"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ideas;"
        results = connectToMySQL(cls.db_name).query_db(query)
        initiatives = []
        for row in results:
            initiatives.append( cls(row))
        return initiatives

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM ideas WHERE ididea = %(ididea)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(results[0])

#    @staticmethod
#    def validate_initiative(initiative):
#        is_valid = True
#        if len(initiative['name']) < 5:
#            flash("Initiative name must be at least 5 character")
#            is_valid= False
#        return is_valid