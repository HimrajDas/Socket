from socket import *
serverName = "192.168.1.5"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input("Write something: ")
clientSocket.send(sentence.encode())
modified_sentense = clientSocket.recv(1024)
print("From server: ", modified_sentense.decode())
clientSocket.close()