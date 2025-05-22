import pymongo, zmq, datetime, os, time

#Establish connection to Mongo and Database, Define outside of code
user = "ReplaceWithUsername"
password = "ReplaceWithPassword"
collection_name = "MicroserviceTest"
database_name = "events"
connection_string = f"mongodb+srv://{user}:{password}@superstore.te53umy.mongodb.net/?retryWrites=true&w=majority&appName=Superstore"
client = pymongo.MongoClient(connection_string)
db = client.get_database(collection_name)
collection = db.events

#Establish ZeroMQ Connection
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")


#Keeps the pipeline waiting and listening
while True:

    message = socket.recv_pyobj()
    if len(message) > 0:

        # insert new event
        if message[0] == 1:
            collection.insert_one(message[1])
            socket.send_string("New event added!")

        # find events by UserID
        elif message[0] == 2:
            results = []
            value = message[1]
            for i in collection.find({"userID": value}):
                print(i)
                results.append(i)
            socket.send_pyobj(results)
            #socket.send_string("Sent all matching entries.")

        #delete event
        elif message[0] == 3:
            value = message[1]
            collection.delete_one({"eventID": value})
            socket.send_string("Entry deleted")

    else:
        print("Waiting for valid data...")

    time.sleep(1)

# Test code for updating data
# current_entry = collection.find_one({"id": "FDgd" })
# new_data = {"$set": {"userID": "UpdatingTest"}}
# collection.update_one(current_entry, new_data)