import argparse
from socket import *

# Usage: python PortScanner.py -a 192.168.0.1 -p 21,80

def printBanner(connSock, targetPort):
    try:
        # Send data to target
        if(targetPort == 80):
            connSock.send('GET HTTP/1.1 \r\n')
        else:
            connSock.send('\r\n')

        # Receive data from target
        results = connSock.recv(4096)
        # Print Banner
        print('[+] Banner: ' + str(results))
    except:
        print('[-] Banner not available \n')

def connScan(targetHost, targetPort):
    try:
        # Create the socket object
        connSock = socket(AF_INET, SOCK_STREAM)
        # Try to connect
        connSock.connect((targetHost, targetPort))
        print('[+] %d tcp open'% targetPort)
        printBanner(connSock, targetPort)
    except:
        # Print the failure
        print('[+] %d tcp closed'% targetPort)
    finally:
        # Close the socket object
        connSock.close()

def portScan(targetHost, targetPort):
    try:
        # if -a was not an IP address...
        targetIP = gethostbyname(targetHost)
    except:
        print('[-] Error: Unknown Host')
        exit(0)

    try:
        # if the domain can be resolved...
        targetName = gethostbyaddr(targetIP)
        print('[+] --- Scan results for: ' + targetName[0] + ' ---')
    except:
        print('[+] --- Scan results for: ' + targetIP + ' ---')

    setdefaulttimeout(10)

    # For each port number call the connScan function
    for targetPort in targetPorts:
        connScan(targetHost, int(targetPort))

def main():
    # Parse the command line arguments
    parser = argparse.ArgumentParser('Smart TCP Client Scanner')
    parser.add_argument('-a', '--address', type = str, help = 'The target IP address')
    parser.add_argument('-p', '--port', type = str, help = 'The port number to connect with')
    args = parser.parse_args()

    # Store the arguments values
    ipaddress = args.address
    portNumbers = args.port.split(',')

    # Call the Port Scan function
    portScan(ipaddress, portNumbers)

if __name__ == "__main__":
    main()