num1 = 42 # variable declaration, numbers
num2 = 2.3 # variable declaration, numbers
boolean = True # variable declaration, boolean
string = 'Hello World' #variable declaration, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # initialize list, strings
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # initialize dictionary, strings, numbers, boolean
fruit = ('blueberry', 'strawberry', 'banana') # initialize list
print(type(fruit)) # log statement, type check
print(pizza_toppings[1]) #log statement
pizza_toppings.append('Mushrooms') #add value
print(person['name']) # log statement
person['name'] = 'George' # Change value
person['eye_color'] = 'blue' #add value
print(fruit[2]) #log statement 

if num1 > 45:# conditional if
    print("It's greater") # log statement
else: #conditional else
    print("It's lower")# log statement

if len(string) < 5: #conditional if 
    print("It's a short word!")# log statement
elif len(string) > 15: # conditional else if
    print("It's a long word!") # log statement
else:# conditional else
    print("Just right!")# log conditional

for x in range(5): #conditional for
    print(x) # log statement
for x in range(2,5): #conditional for
    print(x)# log statement
for x in range(2,10,3):#conditional for
    print(x)#log statement
x = 0#variable declaration
while(x < 5):#  while loop
    print(x)# log statement
    x += 1 #increment

pizza_toppings.pop() #delete value
pizza_toppings.pop(1)# delete value

print(person) #log statement
person.pop('eye_color')# delete value
print(person) #log statement

for topping in pizza_toppings: #conditional for
    if topping == 'Pepperoni': #conditional if
        continue # continue
    print('After 1st if statement') #log statement
    if topping == 'Olives': #conditional if
        break #break

def print_hello_ten_times(): # log statement
    for num in range(10): # conditional for
        print('Hello') # log statement

print_hello_ten_times() # log statement

def print_hello_x_times(x):# function
    for num in range(x): # conditional for 
        print('Hello')# log statement

print_hello_x_times(4) # log statement

def print_hello_x_or_ten_times(x = 10): #function
    for num in range(x): #conditional for
        print('Hello') # log statement

print_hello_x_or_ten_times() # log statement 
print_hello_x_or_ten_times(4)# log statement


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)