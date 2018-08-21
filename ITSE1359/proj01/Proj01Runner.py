class Runner():

    message = " I certify that this program is my own work \n and is not the work of others. I agree not \n to share my solution with others. \n Petra Unglaub-Maycock \n"
    print(message)

    def run(aTuple):
        aTuple[0].pensize(2)
        aTuple[0].color('red')
        aTuple[0].shape('turtle')
        
        aTuple[1].pensize(3)
        aTuple[1].color('green')
        aTuple[1].shape('circle')
        
        aTuple[2].pensize(4)
        aTuple[2].color('blue')
        aTuple[2].shape('triangle')
        
        aList = list(aTuple)
        aList.append('Petra Unglaub-Maycock')

        return aList