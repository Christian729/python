from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja


class Dojo:
    def __init__(self , db_data ):
        self.id = db_data['id']
        self.D_name = db_data['D_name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.ninjas= []

    @classmethod
    def get_all (cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        dojos = []
        
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def save(cls, data):
        query= "INSERT INTO dojos (D_name) VALUES (%(D_name)s);"
        result = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        return result

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        return cls(result[0]) 

    @classmethod
    def get_one_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        print(result)
        dojo = cls(result[0] )
        for f_ninja in result:
            if f_ninja['ninjas.id'] == None:
                break
            data = {
                "id": f_ninja["ninjas.id"],
                "first_name": f_ninja["first_name"],
                "last_name": f_ninja["last_name"],
                "age": f_ninja["age"],
                "created_at": f_ninja["ninjas.created_at"],
                "updated_at": f_ninja["ninjas.updated_at"],
                "dojo_id": f_ninja["dojo_id"]
            }
            
            dojo.ninjas.append(ninja.Ninja(data))
        return dojo

    @classmethod 
    def get_last(cls):
        query = "SELECT * FROM users"
        result = connectToMySQL('dojos_and_ninjas').query_db(query)
        return cls(result[len(result)-1])