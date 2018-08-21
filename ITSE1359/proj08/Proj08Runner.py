def run(myListA, char):
    message: str = "I certify that this program is my own work \nand is not the work of others. I agree not \nto share my " \
                   "solution with others. "
    print( message )

    print( "Petra Unglaub-Maycock \n" )
    print( char )
    print( myListA )

    # create empty list for assignment
    listB = []

    # iterate through list, if element does not contain
    # 'char' then append to list

    listElection: object
    for listElection in myListA:
        if char not in listElection:
            listB.append( listElection )

    return listB
