from flask_app.config.mysqlconnection import connectToMySQL

class Recipe:
    def __init__( self , db_data ):
        self.id = db_data['id']
        self.name = db_data['name']
        self.description = db_data['description']
        self.instructions = db_data['instructions']
        self.under = db_data['under']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.user_id = db_data['user_id']
        self.school = None
    @classmethod
    def save( cls , data ):
        query = "INSERT INTO recipes ( name , description , instructions , under, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(under)s, %(user_id)s);"
        return connectToMySQL('recipes').query_db(query,data)