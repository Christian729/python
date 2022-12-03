from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash


class Show:

    def __init__(self, data):
        self.id = data['id']
        self.s_name = data['s_name']
        self.network = data['network']
        self.release_date = data['release_date']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = user.User.get_by_id({'id':data["user_id"]})

# so i imported some code from the solutions area to try and troubleshoot the problem im having
# which in this case is getting my code to display the html that i want to show.
# i think that its a problem with the code in either my controllers or models.

    @classmethod
    def save( cls , data ):
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        query = """INSERT INTO shows ( s_name , network, release_date, description, user_id) 
        VALUES (%(s_name)s, %(network)s, %(release_date)s, %(description)s, %(user_id)s);"""
        return connectToMySQL('exam2').query_db(query,data)

    @classmethod
    def get_all(cls):
        # Get all shows, and the user info for the creators
        query = """SELECT 
                    shows.id, shows.created_at, shows.updated_at, description, s_name, release_date, network,
                    users.id as user_id, first_name, last_name, email, users.created_at as uc, users.updated_at as uu
                    FROM shows
                    JOIN users on users.id = shows.user_id;"""
        TVshow_data = connectToMySQL('exam2').query_db(query)

        # Make a list to hold recipe objects to return
        shows = []

        # Iterate through the list of recipe dictionaries
        for show in TVshow_data:

            # convert data into a recipe object
            show_obj = cls(show)

            # convert joined user data into a user object
            show_obj.user = user.User(
                {
                    "id": show["user_id"],
                    "first_name": show["first_name"],
                    "last_name": show["last_name"],
                    "email": show["email"],
                    "password": None,
                    "created_at": show["created_at"],
                    "updated_at": show["updated_at"]
                }
            )
            shows.append(show_obj)


        return shows

    @classmethod
    def update(cls, data):
        query = "UPDATE shows SET s_name=%(s_name)s, description=%(description)s, network=%(network)s, release_date=%(release_date)s,updated_at=NOW() WHERE id=%(id)s;"
        return connectToMySQL('exam2').query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM shows WHERE id = %(id)s;"
        result = connectToMySQL('exam2').query_db(query, data)
        return cls(result[0])

    @classmethod 
    def get_last(cls):
        query = "SELECT * FROM shows"
        result = connectToMySQL('exam2').query_db(query)
        return cls(result[len(result)-1])

    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM shows WHERE id = %(id)s;"
        return connectToMySQL('exam2').query_db(query, data)

    @staticmethod
    def validate_show(show):
        is_valid = True

        if len(show['s_name']) < 1:
            flash("Show requires a name!")
            is_valid = False
        if len(show['description']) < 2:
            flash("Description field required!")
            is_valid = False
        if len(show['network']) < 2:
            flash("Network field required!")
        if not show.get('release_date'):
            flash("Date field required!")
            is_valid= False
        

        return is_valid