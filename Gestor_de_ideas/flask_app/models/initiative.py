from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Initiative:
    db_name = "ideas"
    def __init__(self,data):
        self.idinitiative = data['idinitiative']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.id_cluster = data['id_cluster']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO initiative (name, created_at, updated_at, id_cluster) VALUES (%(name)s, NOW(), NOW(), %(id_cluster)s);"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM initiative;"
        results = connectToMySQL(cls.db_name).query_db(query)
        initiatives = []
        for row in results:
            initiatives.append( cls(row))
        return initiatives

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM initiative WHERE idinitiative = %(idinitiative)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(results[0])

    @staticmethod
    def validate_initiative(initiative):
        is_valid = True
        if len(initiative['name']) < 5:
            flash("Initiative name must be at least 5 character")
            is_valid= False
        return is_valid