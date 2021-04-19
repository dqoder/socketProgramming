from socket import *
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

# delete this
clientSocket.bind(('', 29929))

message = input('Input lowercase sentence:\n')
clientSocket.sendto(message.encode(), (serverName, serverPort))

print('clientSocket:', clientSocket)
# print('clientPort:', clientSocket.po)
# print('\twith timeout = ', clientSocket.gettimeout())
# print('\twith blocking = ', clientSocket.getblocking())
print()

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print(modifiedMessage.decode())
print(serverAddress)

clientSocket.close()
