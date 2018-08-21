# import regex
import re
from typing import Any, Iterator


def run(myTuple, myWord):
    message: str = "I certify that this program is my own work \nand is not the work of others. I agree not \nto share my " \
                   "solution with others. "
    print( message )

    print( "Petra Unglaub-Maycock \n" )
    print( myWord )
    print( myTuple )

    myList: Iterator[Any] = filter(lambda x : re.search(myWord, x), myTuple)
    
    return myList
