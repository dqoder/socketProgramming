from socket import *
serverPort = 12001
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print('The (over TCP) server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()

    print('connectionSocket address :', addr)
    print('\ttimeout:', connectionSocket.gettimeout())

    sentence = connectionSocket.recv(1024)
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence)
    connectionSocket.close()
