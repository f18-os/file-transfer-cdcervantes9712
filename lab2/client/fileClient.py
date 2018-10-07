from socket import *
import sys

def sendFileToServer(clientSocket, file_name):
    try:
        with open(file_name, "r") as clientFile:
            print("Sending file...")
            data = clientFile.read()
            clientSocket.send(data.encode('utf-8'))
            clientFile.close()
    except (FileNotFoundError, IOError):
        print("No such file or directory. Try again.")
        clientSocket.send(("File not found. Try again.").encode('utf-8'))
        return
    print("Successfuly sent file to server.")
    return

def connectSocket():
    clientSocket = socket()                 #create a socket object
    clientAddr = ("127.0.0.1", 50000)       #set address and reserve port
    try:
        clientSocket.connect(clientAddr)
        print ("Connected to server.")
    except:
        print ("Error. Server not found.")
        sys.exit()
    return clientSocket

def startClient():
    try:
        file_name = sys.argv[1]                 #get file name from argument
    except:
        print ("Please type a file to send.")
        sys.exit()
    clientSocket = connectSocket()
    clientSocket.send((file_name).encode('utf-8'))     #send file name and choice to server
    sendFileToServer(clientSocket, file_name.encode('utf-8'))
    clientSocket.close()
    print ("Connection closed.")

startClient()
