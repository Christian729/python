
from flask_app.config.mysqlconnection import connectToMySQL
from .thought import Thought
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0._-]+\.[a-zA-Z]+$')
from flask import flash

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.thoughts = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('exam').query_db(query)

        users = []
        
        print(users)
        for user in results:
            users.append( cls(user) )
        
        return users

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name, last_name , email , password) VALUES ( %(first_name)s , %(last_name)s, %(email)s , %(password)s);"
        result =connectToMySQL('exam').query_db( query, data )
        print(result)
        return result

# new code
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL('exam').query_db(query, data )
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL('exam').query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('exam').query_db(query, data)
        

    @classmethod
    def get_one_with_thoughts(cls, data ):
        query = "SELECT * FROM users LEFT JOIN thoughts on users.id = thoughts.user_id WHERE users.id = %(id)s"
        result = connectToMySQL('exam').query_db(query, data)
        user = cls(result[0])
        for row in result:
            data = {
                "id": row['thoughts.id'],
                "description": row['description'],
                "created_at": row['thoughts.created_at'],
                "updated_at": row['thoughts.updated_at'],
                "user_id": row['user_id']
            }
            user.thoughts.append(Thought(data))
        return user

        
    @staticmethod
    def validate_user(user):
        is_valid = True 
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result= connectToMySQL('exam').query_db(query, user)
        
        if len(result) >= 1:
            flash("Email already taken.", "register")
            is_valid=False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!", "register")
            is_valid = False
        if len(user['first_name']) < 2:
            flash("First name must be at least 2 characters", "register")
            is_valid= False
        if len(user['last_name']) < 2:
            flash("Last name must be at least 2 characters", "register")
            is_valid= False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters", "register")
            is_valid= False
        if user['password'] != user['confirm']:
            flash("Passwords don't match", "register")
            is_valid= False

        return is_valid
        