import turtle

class Runner():
#class used to instantiate immutable code for assignments

    message = " I certify that this program is my own work \n and is not the work of others. I agree not \n to share my solution with others. \n Petra Unglaub-Maycock \n"
    print(message)
    
    message = " I certify that this program is my own work \n and is not the work of others. I agree not \n to share my solution with others. \n Petra Unglaub-Maycock \n"
    print(message)

    my_name = "Petra Unglaub-Maycock"
    storeRandom = []

    def __init__(self, new_value):
      
        self.storeRandom.append(new_value)

    
    def run(self):
        
        aTurtle = turtle.Turtle()
        aTurtle.shape("turtle")
        aTurtle.pensize(5)

        aTuple = (self.storeRandom[1], aTurtle, self.my_name)

        return aTuple