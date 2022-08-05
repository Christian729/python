list = [7,1,5,2]
def arrayOfModulus(list):
    for i in range(0, len(list)):
        if (list[i] % 7 ==0):
            print("How do we make 7 even?")
        elif (list[i] %2 ==0):
            print("Subtract the S!")
        else:
            print("Jokes are great")

arrayOfModulus(list)