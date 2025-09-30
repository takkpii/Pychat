import socket
import config

def serverStart():
    # create ipv4 and TCP socket
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    serverSocket.bind((config.HOST , config.PORT))
    # listen to 5 connection maximum
    serverSocket.listen(5)
    print(f"[*] Server Listening On {config.HOST}:{config.PORT}")

    clientSocket , addr = serverSocket.accept()
    print(f"[*] Accepted Client {addr}")

    message = clientSocket.recv(config.BUFFER_SIZE).decode('utf-8')
    print(f"[Client] : {message}")

    clientSocket.close()
    serverSocket.close()

if __name__ == "__main__":
    serverStart()