from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Hip_Exp:
    db_name = "ideas"
    def __init__(self,data):
        self.idhypothesis = data['idhypothesis']
        self.hypothesis = data['hypothesis']
        self.experiment = data['experiment']
        self.learning = data['learning']
        self.id_initiative = data['id_initiative']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO hypothesis (hypothesis, experiment, learning, id_initiative) VALUES (%(hypothesis)s, %(experiment)s, %(learning)s, %(id_initiative)s);"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM hypothesis;"
        results = connectToMySQL(cls.db_name).query_db(query)
        hypothesis = []
        for row in results:
            hypothesis.append( cls(row))
        return hypothesis

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM hypothesis WHERE idhypothesis = %(idhypothesis)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def get_by_initiative(cls, data):
        query = "SELECT * FROM hypothesis WHERE id_initiative = %(id_initiative)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def count_hip(cls):
        query = "select count(*) from hypothesis;"
        result = connectToMySQL(cls.db_name).query_db(query)
        return result
    
