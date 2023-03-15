from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Cluster:
    db_name = "ideas"
    def __init__(self,data):
        self.idcluster = data['idcluster']
        self.name_cluster = data['name_cluster']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO cluster (name_cluster) VALUES (%(name_cluster)s);"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cluster;"
        results = connectToMySQL(cls.db_name).query_db(query)
        clusters = []
        for row in results:
            clusters.append( cls(row))
        return clusters

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM cluster WHERE idcluster = %(idcluster)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def count_initiatives(cls):
        query = "select count(*) from cluster;"
        result = connectToMySQL(cls.db_name).query_db(query)
        return result

    @staticmethod
    def validate_initiative(cluster):
        is_valid = True
        if len(cluster['name']) < 5:
            flash("Cluster name must be at least 5 character")
            is_valid= False
        return is_valid