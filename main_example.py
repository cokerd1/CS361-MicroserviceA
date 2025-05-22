import pymongo, zmq, os, time, datetime

#Establish connection to Mongo and Database
user = "ReplaceWithUsername"
password = "ReplaceWithPassword"
collection_name = "MicroserviceTest"
database_name = "events"
connection_string = f"mongodb+srv://{user}:{password}@superstore.te53umy.mongodb.net/?retryWrites=true&w=majority&appName=Superstore"
client = pymongo.MongoClient(connection_string)
db = client.get_database(collection_name)
collection = db.events

#Establishing connection to ZeroMQ
context = zmq.Context()
print("Connecting to server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#Create an event
def create_event():
    for i in range(0,10):

        new_event = {
            "eventID": f"Test{i%2}",
            "userID": f"Deryk{i%2}",
            "title": f"this is the {i} title",
            "description": f"this is the {i} discription",
            "time": "time as a string",
            "created": datetime.datetime.today().strftime("%m/%d/%Y")
        }

        socket.send_pyobj([1, new_event])
        print("sent")
        print(f"Microservice responded: {socket.recv()}")
        time.sleep(2)

def find_event(userID):
    socket.send_pyobj([2, userID])
    time.sleep(1)
    message = socket.recv_pyobj()
    for each in message:
        print(each)

def delete_event(eventID):
    socket.send_pyobj([3, eventID])
    print(socket.recv())

'''The following are examples of using/calling each

create_event()
find_event("Deryk1")
delete_event("Test1")

'''