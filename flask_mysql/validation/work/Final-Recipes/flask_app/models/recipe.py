from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash


class Recipe:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.created_on = data['created_on']
        self.under = data['under']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = user.User.get_by_id({'id':data["user_id"]})

# so i imported some code from the solutions area to try and troubleshoot the problem im having
# which in this case is getting my code to display the html that i want to show.
# i think that its a problem with the code in either my controllers or models.

    @classmethod
    def save( cls , data ):
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        query = """INSERT INTO recipes ( name , description, instructions , under, created_on , user_id) 
        VALUES (%(name)s, %(description)s, %(instructions)s, %(under)s, %(created_on)s, %(user_id)s);"""
        return connectToMySQL('recipes').query_db(query,data)

    @classmethod
    def get_all(cls):
        # Get all recipes, and the user info for the creators
        query = """SELECT 
                    recipes.id, recipes.created_at, recipes.updated_at, instructions, description, name, created_on, under,
                    users.id as user_id, first_name, last_name, email, users.created_at as uc, users.updated_at as uu
                    FROM recipes
                    JOIN users on users.id = recipes.user_id;"""
        recipe_data = connectToMySQL('recipes').query_db(query)

        # Make a list to hold recipe objects to return
        recipes = []

        # Iterate through the list of recipe dictionaries
        for recipe in recipe_data:

            # convert data into a recipe object
            recipe_obj = cls(recipe)

            # convert joined user data into a user object
            recipe_obj.user = user.User(
                {
                    "id": recipe["user_id"],
                    "first_name": recipe["first_name"],
                    "last_name": recipe["last_name"],
                    "email": recipe["email"],
                    "password": None,
                    "created_at": recipe["created_at"],
                    "updated_at": recipe["updated_at"]
                }
            )
            recipes.append(recipe_obj)


        return recipes

    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, created_on=%(created_on)s, under=%(under)s,updated_at=NOW() WHERE id=%(id)s;"
        return connectToMySQL('recipes').query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        result = connectToMySQL('recipes').query_db(query, data)
        return cls(result[0])

    @classmethod 
    def get_last(cls):
        query = "SELECT * FROM recipes"
        result = connectToMySQL('recipes').query_db(query)
        return cls(result[len(result)-1])

    # @classmethod
    # def get_by_id(cls, data):
    #     query = "SELECT * FROM recipes WHERE user_id = %(user_id)s;"
    #     result = connectToMySQL('recipes').query_db(query, data)
    #     if len(result) < 1:
    #         return False
    #     return cls(result[0])

    @staticmethod
    def validate_recipe(recipe):
        is_valid = True

        if len(recipe['name']) < 1:
            flash("Recipe requires a name!")
            is_valid = False
        if len(recipe['description']) < 2:
            flash("Description field required!")
            is_valid = False
        if len(recipe['instructions']) < 2:
            flash("Instruction field required!")
            is_valid = False
        if len(recipe["created_on"]) <=0:
            flash("Date field required!")
            is_valid = False
        if not recipe.get('under'):
            flash("Time field required!")
            is_valid= False
        return is_valid