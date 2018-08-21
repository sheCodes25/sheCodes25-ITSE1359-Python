import dbm.dumb
import Proj12Runner

databaseName = 'database'
Proj12Runner.run(databaseName)

dumbDb = dbm.dumb.open(databaseName, 'r')

items = dumbDb.items()

for item in items:
    print(item)

dumbDb.close()

