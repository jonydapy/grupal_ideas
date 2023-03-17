from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Initiative:
    db_name = "ideas"
    def __init__(self,data):
        self.idinitiative = data['idinitiative']
        self.name = data['name']
        self.id_cluster = data['id_cluster']
        self.id_cluster = data['id_rating']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO initiative (name, id_cluster, id_rating) VALUES (%(name)s, %(id_cluster)s, %(id_rating)s);"
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
    def get_by_id(cls, data):
        query = "SELECT * FROM initiative WHERE idinitiative = %(id_initiative)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def count_initiatives(cls):
        query = "select count(*) from initiative;"
        result = connectToMySQL(cls.db_name).query_db(query)
        return result
    
    @classmethod
    def get_initiative_w_cluster(cls):
        query = "select initiative.name as name, initiative.id_cluster as id_cluster, cluster.name_cluster as name_cluster from initiative join cluster on cluster.idcluster = initiative.id_cluster;"
        results = connectToMySQL(cls.db_name).query_db(query)
        initiatives = []
        for result in results:
            datos = {
                "name" : result['name'],
                "id_cluster" : result['id_cluster'],
                "name_cluster" : result['name_cluster']
            }
            initiatives.append( datos )
        return initiatives
    
    @staticmethod
    def validate_initiative(initiative):
        is_valid = True
        if len(initiative['name']) < 5:
            flash("Initiative name must be at least 5 character")
            is_valid= False
        return is_valid