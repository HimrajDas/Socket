from socket import *
serverName = gethostbyname(gethostname())
serverPort = 12000
ADDRESS = (serverName, serverPort)

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(ADDRESS)
serverSocket.listen(1)
print(f"[LISTENING] Server is listening on {serverName}...")

while True:
    connectionSocket, addr = serverSocket.accept()
    print(f"[NEW CONNECTION] {addr} connected.")
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()
