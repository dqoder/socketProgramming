from socket import *
serverName = 'localhost'
serverPort = 12001
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
# 3-way handshaking done by now
# BETWEEN clientSocket and connectionSocket (see TCPServer.py)


sentence = input('Input lowercase sentence: ')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print(f'From server[{0}]:', modifiedSentence.decode())
clientSocket.close()
