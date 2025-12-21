"""
This example demonstrates a UDP server
"""

import socket
#Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#Bind to IP and Port
sock.bind(('127.0.0.1',9999))
#Main loop
while True:
    #Receive data from a client
    recv_data, client_info = sock.recvfrom(1024)
    print(f'Client{client_info[0]} says: {recv_data.decode('utf-8')}')

    #Send a response to the client
    sock.sendto('Hello, client'.encode('utf-8'), client_info)

#Close the socket(note: this step is unreachable due to infinite loop)
sock.close()