import socket

print("DNS Server Started!!")
address = ("127.0.0.1", 65000)	#Here your own ip addresss instead of "127.0.0.1" and can also change port in place of 65000
bufferSize = 1024   #size of buffer for receiving queries

UDP_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Socket Creation: AF_INET for ipv4 addressing, SOCK_DGRAM for UDP
UDP_sock.bind(address)   #binding socket to ip and port

type_A = {"http://www.a.com":"1.1.1.1", "http://www.b.com":"2.2.2.2", "http://www.c.com":"3.3.3.3"} #Type A records
type_CNAME = {"http://www.d.com":"http://www.dalias.com", "http://www.e.com":"http://www.ealias.com", "http://www.f.com":"http://www.falias.com"}   #CNAM records

while True:
    print("---------------------------------------------------------------------------")
    print("Listening for client at ip=" + address[0] + " and port=" + str(address[1]) + " ...")
    query, client_address = UDP_sock.recvfrom(bufferSize) #receiving client's query
    print("Client query: " + query.decode())

    ##checking type of query: A or CNAME and preparing response
    URL = query.decode()
    if(URL in type_A.keys()):
        response = "A," + type_A[URL]
    elif(URL in type_CNAME.keys()):
        response = "CNAME," + type_CNAME[URL]
    else:
        response = "None,None"

    UDP_sock.sendto(response.encode(), client_address) #response sending to client