from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash


class Thought:

    def __init__(self, data):
        self.id = data['id']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        # self.user = None
        self.user = user.User.get_by_id({'id':data["user_id"]})



    @classmethod
    def save( cls , data ):
        query = """INSERT INTO thoughts ( description, user_id) 
        VALUES (%(description)s, %(user_id)s);"""
        return connectToMySQL('exam').query_db(query,data)

    @classmethod
    def get_all_thoughts_with_creator(cls):
        # Get all tweets, and their one associated User that created it
        query = "SELECT * FROM thoughts JOIN users ON users.id = thoughts.user_id;"
        results = connectToMySQL('exam').query_db(query)
        thoughts = []
        for row in results:
            thought = cls(row)
            user_data = {
                # Any fields that are used in BOTH tables will have their name changed, which depends on the order you put them in the JOIN query, use a print statement in your classmethod to show this.
                "id": row['users.id'], 
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "email": row['email'],
                "password": None,
                "created_at": row['users.created_at'],
                "updated_at": row['users.updated_at']
            }

            user_obj = user.User(user_data)
            # Append the Tweet containing the associated User to your list of tweets
            thought.user = user_obj
            thoughts.append(thought)
        return thoughts
    @classmethod
    def get_all(cls):
        # Get all thoughts, and the user info for the creators
        query = """SELECT 
                    thoughts.id, thoughts.created_at, thoughts.updated_at, description,
                    users.id as user_id, first_name, last_name, email, users.created_at as uc, users.updated_at as uu
                    FROM thoughts
                    JOIN users on users.id = thoughts.user_id;"""
        thought_data = connectToMySQL('exam').query_db(query)

        thoughts = []

        # Iterate through the list of recipe dictionaries
        for thought in thought_data:

            # convert data into a recipe object
            thought_obj = cls(thought)

            # convert joined user data into a user object
            thought_obj.user = user.User(
                {
                    "id": thought["user_id"],
                    "first_name": thought["first_name"],
                    "last_name": thought["last_name"],
                    "email": thought["email"],
                    "password": None,
                    "created_at": thought["created_at"],
                    "updated_at": thought["updated_at"]
                }
            )
            thoughts.append(thought_obj)


        return thoughts

    @classmethod
    def update(cls, data):
        query = "UPDATE thoughts SET description=%(description)s, updated_at=NOW() WHERE id=%(id)s;"
        return connectToMySQL('exam').query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM thoughts WHERE id = %(id)s;"
        result = connectToMySQL('exam').query_db(query, data)
        return cls(result[0])

    @classmethod 
    def get_last(cls):
        query = "SELECT * FROM thoughts"
        result = connectToMySQL('exam').query_db(query)
        return cls(result[len(result)-1])

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM thoughts WHERE user_id = %(user_id)s;"
        result = connectToMySQL('exam').query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])
# added a delete
    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM thoughts WHERE id = %(id)s;"
        return connectToMySQL('exam').query_db(query, data)

    @staticmethod
    def validate_thought(thought):
        is_valid = True

        if not thought.get('description'):
            flash("Thought field required!")
            is_valid = False
        if len(thought['description']) < 5:
            flash("Thought must be at least 5 characters!")
            is_valid = False

        return is_valid