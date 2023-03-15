from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Idea:
    db_name = "ideas"
    def __init__(self,data):
        self.ididea = data['ididea']
        self.content = data['content']
        self.user_id = data['user_id']
        self.id_campaing = data['id_campaing']
        self.id_cluster = data['id_cluster']
        self.comment = data['comment']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO ideas (content, user_id, id_campaing, id_cluster) VALUES (%(content)s,%(user_id)s,%(id_campaing)s,%(id_cluster)s);"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def get_allideasporusuario(cls): #trae numero de idea,descripcion, nombre y apellido del creador de la idea en ideas.html
        query = "select ididea, content, first_name, last_name from ideas join users on user_id = iduser"
        results = connectToMySQL(cls.db_name).query_db(query)
        ideas = []
        for row in results:
            ideas.append( cls(row))
        return ideas
    @classmethod
    def get_allcampaing(cls): #trae numero de idea,descripcion, nombre y apellido del creador de la idea en ideas.html
        query = "select * from campaigns"
        results = connectToMySQL(cls.db_name).query_db(query)
        campaigns = []
        for row in results:
            campaigns.append((row))
        return campaigns
    @classmethod
    def get_by_ididea(cls,data):
        query = "SELECT * FROM ideas WHERE ididea = %(ididea)s;" 
        #hacer join para traer nombre del us    uario ej: SELECT distinct(si se repiten nombres) m.grupo_id, u.first_name, u.last_name FROM miembros m JOIN users u ON m.user_id=u.id order by m.grupo_id;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return (results[0])
    @classmethod
    def save_comment(cls,data):
        query = "insert into comments (comment, user_id, ididea ) values (%(comment)s,%(user_id)s,%(ididea)s)"
        return connectToMySQL(cls.db_name).query_db(query,data)
        

#    @staticmethod
#    def validate_initiative(initiative):
#        is_valid = True
#        if len(initiative['name']) < 5:
#            flash("Initiative name must be at least 5 character")
#            is_valid= False
#        return is_valid