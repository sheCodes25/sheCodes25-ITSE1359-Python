# import the dumb module
import dbm.dumb

def populateIt(myKeys, myValues, databaseName):
    message: str = "I certify that this program is my own work \nand is not the work of others. I agree not \nto share my " \
                   "solution with others. "
    print( message )
    print( 'Petra Unglaub-Maycock \n' )

    # open the dumb DB
    dumbDB = dbm.dumb.open( databaseName, 'c' )

    # Populate the database
    for cnt in range( len( myKeys ) ):
        dumbDB[myKeys[cnt]] = myValues[cnt]

    # loop and assign values to the DB file
    for index in range( len( myKeys ) ):
        dumbDB[myKeys[index]] = myValues[index]
    dumbDB.close()

def printIt(myKeys, myValues, databaseName):
    dumbDB = dbm.dumb.open( databaseName, 'c' )
    # loop and print the key and value
    for key, value in dumbDB.items():
        print( "key: " + str( key ) + " value: " + str( value ) )
    dumbDB.close()

