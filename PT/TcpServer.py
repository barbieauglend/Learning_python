import socket
import threading
import argparse

def serveClient(clientToServeSocket, clientIPAddress, portNumber):
    clientRequest = clientToServeSocket.recv(4096)
    print('[!] Received dara from the client (%s:%d) : %s' % clientIPAddress, portNumber, clientRequest)

    # Reply back to client
    clientToServeSocket.send('I am a server!')
    # Close socket
    clientToServeSocket.close()

def startServer(portNumber):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', portNumber))
    server.listen(10)
    print('[!] Listening locally on port %d ...' % portNumber)

    while True:
        client,address = server.accept()
        print('[+] Connected with the client: %s:%d' % (address[0],address[1]))

        # Handle clients
        serveClientThread = threading.Thread(target=serveClient, args(client, address[0], address[1]))
        serveClientThread.start()

def main():
    # Parse the command line arguments
    parser = argparse.ArgumentParser('TCP server')
    parser.add_argument('-p', '--port', type = int, help='The port number' )
    args = parser.parse_args()

    # Store he argument value
    portNumber = args.port

    # Start the server
    startServer(portNumber)

if __name__ == "__main__":
    main()
