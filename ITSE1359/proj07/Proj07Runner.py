from typing import List, Any

message: str = "I certify that this program is my own work \nand is not the work of others. I agree not \nto share my " \
               "solution with others. "
print( message )

def run(str,index):
    
    print( "Petra Unglaub-Maycock \n" )
    print(str)
    print(index)
    
    #create empty lsit for assignment
    myList: List[Any] = []
    
    myList.append(str[:index])
    myList.append(str[index-1:])
    
    return myList