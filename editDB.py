from DBClient import DBClient

DB_URI = "mongodb://167.99.69.49:27017/"
DB_NAME = 'CSTIX'
# Create a new client and connect to the server
db_client = DBClient(DB_URI, DB_NAME)


def editEvent():
    
    op = input('operation: ')
    Events = db_client.get_collection('Events')
    if op == 'edit':
        name = input('name: ')
        attr = input('attribute: ')
        val = input('value')
        try:
            result = Events.updateOne(
                {'name:' : name},
                {
                    '$set': {attr: val}
                }
            )

        except Exception as e:
            print(e)
    elif op == 'delete':
        names = []
        while True:
            event = input('name: ')
            if event == '':
                break
            names.append(event)
        try:
            Events.delete_many(
                {
                    'name':{'$in': names}
                }
            )
        except Exception as e:

            print(e)
    return

def editUser(name):
    return

if __name__ == "__main__":
    
    editEvent()