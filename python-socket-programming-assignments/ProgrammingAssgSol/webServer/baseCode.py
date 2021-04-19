# import socket module
from socket import *
import sys  # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a server socket
serverSocket.bind(('', 80))
serverSocket.listen(1)

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(2**12)

        print('message: ')
        print(message.decode())

        filename = message.split()[1][1:].decode()

        print('filename: ', filename)
        if filename == '':
            filename = 'index.html'
        try:
            f = open(filename)
        except:
            print('---error---: ', filename, 'not found')
            connectionSocket.close()

        # Send one HTTP header line into socket
        outputdata = f.read()
        outputdata = f'HTTP/1.1 200 OK\r\nServer: LoFer\r\nContent-Type: text/html\r\nContent-Length: {len(outputdata)}\r\Connection: Keep-Alive\r\n\r\n' + \
            outputdata

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        f.close()

    except IOError:
        connectionSocket.send('HTTP/1.1 404 PAGE NOT FOUND\r\n\r\n'.encode())
    finally:
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data
