# CS361-MicroserviceA
This microservice will help do some basic CRUD operations when connecting to MongoDB

# Setup
Before using the code in the microservice, you need to setup your MongoDB account. You'll need to create a collection and then a database as well for this program to work.
Once those are created, you should be prompted for a username and password, go ahead and add those into the code (environment variables would be best.)
You'll also need to edit the next 3 variables. The collection name, the database name you want to work with, and then the connection string. The connection string you can get
on MongoDB by clicking on Clusters on the left hand side, then Connect, then Drivers.

# Request and Receive Data

I have included the sample code I used during the demonstration, the ZeroMQ code we used during assignment 4 is being used here with the same principles,
but the meat of the code is as follows:
Each request is sent as an array. THe first index is an int of 1, and the 2nd varies.
  Int 1 is used to create an event, and will have full event data sent with it as a dictionary. A string is sent back to confirm event added.
  ```
        new_event = {
            "eventID": "Test",
            "userID": "User",
            "title": "this is the title",
            "description": "this is the discription",
            "time": "time as a string",
            "created": datetime.datetime.today().strftime("%m/%d/%Y")
        }

        socket.send_pyobj([1, new_event])
        print("sent")
        print(f"Microservice responded: {socket.recv()}")
```
  Int 2 is used for finding events, and will have a string sent along with it. The string is which UserID to search for. An array is sent back, containing all events found.
  ```
    socket.send_pyobj([2, userID])
    time.sleep(1)
    message = socket.recv_pyobj()
    for each in message:
        print(each)
  ```
  
  Int 3 is user for deleting events, and will also have a string sent along with it. The string is which EventID to search for. A string is sent back, letting the user know the event was deleted.
  ```
  socket.send_pyobj([3, eventID])
  print(socket.recv())
  ```

# UML Diagram
![image](https://github.com/user-attachments/assets/c3c5c0c8-81e9-4a10-b7cd-5a1564824860)
