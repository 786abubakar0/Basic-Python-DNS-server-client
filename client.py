import socket

address = ("127.0.0.1", 65000)	#change "127.0.0.1" to the ip of the server and 65000 to server port i.e. ip and port specified in the server.py
bufferSize = 1024   #size of buffer for receiving queries' response

UDP_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Socket Creation: AF_INET for ipv4 addressing, SOCK_DGRAM for UDP

while True:
    print("---------------------------------------------------------------------------")
    query  = input("Enter hostname/alias name : ")
    UDP_sock.sendto(query.encode(), address)    #query sending to server

    query_response, server_address = UDP_sock.recvfrom(bufferSize)  #receing server's response
    print("Server Response on you Query : " + str(query_response.decode()))

    ##Asking from user to continue or not
    is_next  = input("Continue? Y/N: ")
    if(is_next != "Y" and is_next!="y"):
        break

