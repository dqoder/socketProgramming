from socket import *
serverPort = 12010
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The OTHER server is ready to receive')

# while True:
# message, clientAddress = serverSocket.recvfrom(2048)
# print('clientAddress: ', clientAddress)
# modifiedMessage = message.decode().upper()
clientAddress = ('localhost', 29929)
serverSocket.sendto('NOT desired'.encode(), clientAddress)
