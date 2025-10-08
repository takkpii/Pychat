import socket
import config

def startClinet ():
    # create socket
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to server
    clientSocket.connect((config.HOST, config.PORT))
    print("Client connected")
    # send message and close connection
    message = "Hello World"
    clientSocket.send(message.encode('utf-8'))
    clientSocket.close()

if __name__ == "__main__":
    startClinet()