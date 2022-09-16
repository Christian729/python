from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.full_name = data['full_name']
        self.location = data['location']
        self.fav_lang = data['fav_lang']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojo_survey').query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        
        
        for user in results:
            users.append( cls(user) )
        return users