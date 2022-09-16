from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0._-]+\.[a-zA-Z]+$')
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('recipes').query_db(query)

        users = []
        
        print(users)
        for user in results:
            users.append( cls(user) )
        
        return users

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name, last_name , email , password, created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s, %(email)s , %(password)s, NOW() , NOW() );"
        result =connectToMySQL('recipes').query_db( query, data )
        print(result)
        return result

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL('recipes').query_db(query, data)
        return cls(result[0])


    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('recipes').query_db(query, data)
        
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL('recipes').query_db(query, data )
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL('recipes').query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, updated_at=NOW() WHERE id=%(id)s;"
        return connectToMySQL('recipes').query_db(query, data)

    @classmethod 
    def get_last(cls):
        query = "SELECT * FROM users"
        result = connectToMySQL('recipes').query_db(query)
        return cls(result[len(result)-1])
        
    @staticmethod
    def validate_user(user):
        is_valid = True 
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result= connectToMySQL('recipes').query_db(query, user)
        
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
        