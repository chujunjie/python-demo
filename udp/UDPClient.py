from socket import *

serverName = "localhost"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)  # AF_INET表示底层网络使用IPv4，SOCK_DGRAM表示一个UDP套接字
message = input("Input lowercase sentence: ")

clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode(), serverAddress)
clientSocket.close()
