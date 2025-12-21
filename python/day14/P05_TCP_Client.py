"""
This case demonstrates the TCP programming client side
"""
import socket
socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '127.0.0.1'
server_port = 9999
socket_tcp.connect((server_ip,server_port))

while True:
    #Send message to the server
    send_data = input(f'Client says:>>> Server says:').encode('utf-8')
    socket_tcp.send(send_data)

    #Receive message from the server
    recv_data = socket_tcp.recv(1024)
    print(f'Server says:{recv_data.decode("utf-8")}')

socket_tcp.close()