from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The server is ready to receive')

while True:
    print('waiting for message...')
    message, clientAddress = serverSocket.recvfrom(2048)
    message = message.decode()
    modifiedMessage = message.upper().encode()
    serverSocket.sendto(modifiedMessage, clientAddress)
