"""
This case demonstrates the TCP programming server side
"""

#Most basic implementation of the server side
import socket
socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Bind ip and port
socket_tcp.bind(('127.0.0.1',9999))
#Set listening to monitor client requests
socket_tcp.listen(5)
#Wait for client connection
socket_client, client_info = socket_tcp.accept()
#Loop
while True:
    #Receive data from a client
    recv_data = socket_client.recv(1024)
    print(f'Client{client_info[0]}says:{recv_data.decode('utf-8')}')

    #Send message to the client
    socket_client.send("Hello".encode('utf-8'))

#Close the socket
socket_client.close()
socket_tcp.close()