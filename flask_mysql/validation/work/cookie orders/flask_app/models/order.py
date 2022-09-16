from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash



class Order:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.cookie_type = data['cookie_type']
        self.num_box = data['num_box']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM orders;"
        results = connectToMySQL('cookie_orders').query_db(query)

        orders = []
        
        print(orders)
        for order in results:
            orders.append( cls(order) )
        
        return orders

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO orders (name, cookie_type , num_box , created_at, updated_at ) VALUES ( %(name)s , %(cookie_type)s, %(num_box)s , NOW() , NOW() );"
        result =connectToMySQL('cookie_orders').query_db( query, data )
        print(result)
        return result

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM orders WHERE id = %(id)s;"
        result = connectToMySQL('cookie_orders').query_db(query, data)
        return cls(result[0])


    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM orders WHERE id = %(id)s;"
        return connectToMySQL('cookie_orders').query_db(query, data)
        
    
    @classmethod
    def update(cls, data):
        query = "UPDATE orders SET name=%(name)s, cookie_type=%(cookie_type)s, num_box=%(num_box)s, updated_at=NOW() WHERE id=%(id)s;"
        return connectToMySQL('cookie_orders').query_db(query, data)

    @classmethod 
    def get_last(cls):
        query = "SELECT * FROM orders"
        result = connectToMySQL('cookie_orders').query_db(query)
        return cls(result[len(result)-1])
        

    @staticmethod
    def validate_order(order):
        is_valid = True # we assume this is true
        if len(order['name']) == 0:
            flash("Name is required.")
            is_valid = False
        elif len(order['name']) < 2:
            flash("Name must be at least 2 characters.")
            is_valid = False
            
        if len(order['cookie_type']) == 0:
            flash("Cookie type is required.")
            is_valid = False
        elif len(order['cookie_type']) < 2:
            flash("Cookie type must be at least 2 characters.")
            is_valid = False
        
        if int(order['num_box']) < 1:
            flash("Must choose at least one box.")
            is_valid = False
        elif len(order['num_box']) == 0:
            flash("Please enter a valid number of boxes.")
            is_valid = False
        return is_valid

# so my problem was trying to understand how to make the int
# be equal to or greater than 1 to be valid. but it only 
# understands the length of the string when using the len(order)
# so maybe theres another command i can use.
    