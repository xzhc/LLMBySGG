"""
This example demonstrates a UDP client
"""

import socket


#Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Server address
server_ip = '127.0.0.1'
server_port = 9999

#Main loop
while True:
    #Send user input to the server
    msg = input('Client says: ')
    sock.sendto(msg.encode('utf-8'), (server_ip, server_port))

    #Receive response from the server
    recv_data, server_info = sock.recvfrom(1024)
    print(f'Server {server_info[0]} says: {recv_data.decode("utf-8")}')

#Close the socket(note: the step is unreachable due to infinite loop)
sock.close()