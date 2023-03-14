from flask_app.config.mysqlconnection import connectToMySQL

class Type_User:
    db_name = "ideas"
    def __init__(self,data):
        self.idtipo = data['idtipo']
        self.description = data['description']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM type_user;"
        results = connectToMySQL(cls.db_name).query_db(query)
        users = []
        for row in results:
            users.append( cls(row))
        return users