from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Comment:
    db_name = "ideas"
    def __init__(self,data):
        self.idcomment = data['idcomment']
        self.comment = data['comment']
        self.user_id = data['user_id']
        self.idea_id = data['idea_id']

    @classmethod
    def savecomment(cls,data):
        query = "INSERT INTO comments (comment, user_id, idea_id) VALUES (%(comment)s,%(user_id)s,%(idea_id)s);"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def get_allcommentsporidea(cls,data): #trae todos los comentarios de la ididea
        query = """select comment, user_id, idea_id, first_name, last_name,idcomment from comments 
        join users on user_id = iduser where idea_id = %(ididea)s;"""
        print(query)
        results = connectToMySQL(cls.db_name).query_db(query,data)
        print(results)
        comments = []
        for row in results:
            comments.append( (row))
        return comments