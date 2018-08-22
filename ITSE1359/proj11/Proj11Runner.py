import dbm.dumb

def run(myKeys,myValues,databaseName):
    message: str = "I certify that this program is my own work \nand is not the work of others. I agree not \nto share my " \
                   "solution with others. "
    print( message )
    print( 'Petra Unglaub-Maycock \n' )

    myKeys = b'gender',b'name',b'age'
    myValues = b'male',b'Joe',b'39'

    # open the dumb DB
    dumbDb = dbm.dumb.open( databaseName, 'c' )

    # populate the database
    for i in range( len( myKeys ) ):
        dumbDb[myKeys[i]] = myValues[i]

    dumbDb.close()

