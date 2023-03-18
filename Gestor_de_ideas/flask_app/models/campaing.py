from flask_app.config.mysqlconnection import connectToMySQL

class Campaign:
    db_name = "ideas"
    def __init__(self,data):
        self.idcampaign = data['idcampaign']
        self.name_campaing = data['name_campaing']
        self.description = data['description']
        self.id_strategy= data['id_strategy']

    @classmethod
    def get_allcampaing(cls): #trae numero de idea,descripcion, nombre y apellido del creador de la idea en ideas.html
        query = "select * from campaigns;"
        results = connectToMySQL(cls.db_name).query_db(query)
        campaigns = []
        for row in results:
            campaigns.append(cls(row))
        return campaigns
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO campaigns (name_campaing, id_strategy) VALUES (%(campaign)s, %(idstrategy)s);"
        print(query)
        return connectToMySQL(cls.db_name).query_db(query,data)
        
    @classmethod
    def count_campaings(cls):
        query = "select count(*) from campaigns;"
        result = connectToMySQL(cls.db_name).query_db(query)
        return result