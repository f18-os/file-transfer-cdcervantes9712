from socket import *
import sys

def getFileFromClient(conn, file_name):
    if file_name == "File not found. Try again.":
        print(file_name)
        return
    with open(file_name, "w") as serverFile:
        serverFile.write(str(file_name))
        while True:
            print("Receiving data...")
            data = conn.recv(1024)
            if file_name == "File not found. Try again.":
                return
            if not data:
                break
            print("Data = " + str(data))
            # write data to a file
            serverFile.write(str(data))
    serverFile.close()
    print("Successfully get file from client.")
    return

def socketListen():
    serverAddr = ("127.0.0.1", 50000)           #set host and address
    serverSocket = socket()                     #create a socket object
    serverSocket.bind(serverAddr)               #bind to the port
    serverSocket.listen(1)                      #wait for client connection.
    print("Server listening....")
    return serverSocket

def startServer():
    serverSocket = socketListen()
    while True:
        conn, addr = serverSocket.accept()      #establish connection with client.
        print("Got connection from", addr)
        file_name = conn.recv(1024)
        getFileFromClient(conn, file_name)
        serverSocket.close()
        print("Connection closed.")
        sys.exit()
startServer()
