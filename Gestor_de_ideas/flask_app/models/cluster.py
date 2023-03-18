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
    def count_cluster(cls):
        query = "select count(*) from cluster;"
        result = connectToMySQL(cls.db_name).query_db(query)
        return result
    
    @classmethod
    def get_ideas_in_cluster(cls, data):
        query = "SELECT ideas.content as idea_name, cluster.name_cluster as name_cluster, cluster.idcluster as idcluster FROM ideas INNER JOIN cluster ON ideas.id_cluster = cluster.idcluster WHERE ideas.id_cluster = %(id_cluster)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        ideas = []
        for result in results:
            users_data = {
                "idea_name" : result['idea_name'],
                "name_cluster" : result['name_cluster'],
                "idcluster" : result['idcluster']
            }
            ideas.append( users_data )
        print(results)
        return ideas
    
    @classmethod
    def get_ideas_to_cluster(cls):
        query = "select ideas.content as idea, ideas.ididea as ididea, cluster.idcluster as idcluster, cluster.name_cluster as name_cluster, ideas.user_id as user_id, users.first_name as first_name, users.last_name as last_name from ideas join cluster on cluster.idcluster = ideas.id_cluster join users on users.iduser = ideas.user_id;"
        results = connectToMySQL(cls.db_name).query_db(query)
        ideas = []
        for result in results:
            users_data = {
                "idea" : result['idea'],
                "ididea" : result['ididea'],
                "idcluster" : result['idcluster'],
                "name_cluster" : result['name_cluster'],
                "user_id" : result['user_id'],
                "first_name" : result['first_name'],
                "last_name" : result['last_name']
            }
            ideas.append( users_data )
        print(results)
        return ideas
    
    @staticmethod
    def validate_initiative(cluster):
        is_valid = True
        if len(cluster['name']) < 5:
            flash("Cluster name must be at least 5 character")
            is_valid= False
        return is_valid