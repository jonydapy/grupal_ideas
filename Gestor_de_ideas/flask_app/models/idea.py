from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Idea:
    db_name = "ideas"
    def __init__(self,data):
        self.ididea = data['ididea']
        self.content = data['content']
        self.user_id = data['user_id']
        self.id_campaign = data['id_campaign']
        self.id_cluster = data['id_cluster']
        #self.comment = data['comment']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO ideas (content, user_id, id_campaign, id_cluster) VALUES (%(content)s,%(id)s,%(id_campaign)s,1 );"
        print(query)
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def get_allideasporusuario(cls,data): #trae numero de idea,descripcion, nombre y apellido del creador de la idea en ideas.html
        query = """select ididea, content, user_id,id_campaign,id_cluster, first_name, last_name from ideas join users on user_id = iduser 
        where id_campaign=(%(id_campaign)s);"""
        print(query)
        results = connectToMySQL(cls.db_name).query_db(query,data)
        print(results)
        ideas = []
        for row in results:
            ideas.append( (row))
        return ideas
    @classmethod
    def get_by_ididea(cls,data):
        query = "select ididea, content, first_name, last_name from ideas join users on user_id = iduser where ididea= %(ididea)s" 
        results = connectToMySQL(cls.db_name).query_db(query,data)
        ideas = []
        for row in results:
            ideas.append( (row))
        return ideas
    
    @classmethod # Jony
    def update_cluster(cls, data):
        query = "update ideas set id_cluster = %(idcluster)s where (ididea = %(ididea)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def count_ideas(cls):
        query = "select count(*) from ideas;"
        result = connectToMySQL(cls.db_name).query_db(query)
        return result
    
    @classmethod
    def count_ideas_por_id(cls, data):
        query = "select count(*) from ideas where user_id = %(user_id)s;"
        result = connectToMySQL(cls.db_name).query_db(query, data)
        return result
    
#@classmethod
#def save_comment(cls,data):
#    query = "insert into comments (comment, user_id, ididea ) values (%(comment)s,%(user_id)s,%(ididea)s)"
#    return connectToMySQL(cls.db_name).query_db(query,data)

#    @staticmethod
#    def validate_initiative(initiative):
#        is_valid = True
#        if len(initiative['name']) < 5:
#            flash("Initiative name must be at least 5 character")
#            is_valid= False
#        return is_valid