from flask_app.config.mysqlconnection import connectToMySQL
import re	# the regex module
from flask import flash

# Expersion regular para validar correos   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    db_name = "ideas"
    def __init__(self,data):
        self.iduser = data['iduser']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.type_user = data['type_user']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at, type_user) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s, NOW(), NOW(), %(type_user)s);"
        result = connectToMySQL(cls.db_name).query_db(query, data)
        data_user = {
            "id" : result
        }
        return cls.get_by_id(data_user)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db_name).query_db(query)
        users = []
        for row in results:
            users.append( cls(row))
        return users

    @classmethod
    def get_by_email(cls, u_email):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        data_user = {
            "email" : u_email
        }
        result = connectToMySQL(cls.db_name).query_db(query, data_user)
        if len(result) > 0:
            return cls(result[0])
        else:
            return None

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE iduser = %(id)s;"
        result = connectToMySQL(cls.db_name).query_db(query, data)
        if len(result) > 0:
            return cls(result[0])
        else:
            return None
        
    @classmethod
    def get_name_lastname_role(cls):
        query = "select users.iduser as iduser, users.first_name as first_name, users.last_name as last_name, type_user.idtipo as idtipo, type_user.description as type_user from users join type_user on users.type_user = type_user.idtipo;"
        results = connectToMySQL(cls.db_name).query_db(query)
        users = []
        for result in results:
            users_data = {
                "iduser" : result['iduser'],
                "first_name" : result['first_name'],
                "last_name" : result['last_name'],
                "idtipo" : result['idtipo'],
                "type_user" : result['type_user']
            }
            users.append( users_data )
        return users
    
    @classmethod
    def update_role(cls, data):
        query = "update users set type_user = %(idtipo)s where iduser = %(iduser)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def update_profile(cls, data): 
        query = "update users set first_name = %(first_name)s , last_name = %(last_name)s , email = %(email)s  where iduser = %(iduser)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)
    

    @staticmethod
    def validate_register(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(User.db_name).query_db(query, user)
        if len(results) >= 1:
            flash("Email already taken.","register")
            is_valid= False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid Email!!!","register")
            is_valid= False
        if len(user['first_name']) < 3:
            flash("First name must be at least 3 characters","register")
            is_valid= False
        if len(user['last_name']) < 3:
            flash("Last name must be at least 3 characters","register")
            is_valid= False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters","register")
            is_valid= False
        if user['password'] != user['conf-password']:
            flash("Passwords don't match","register")
        return is_valid