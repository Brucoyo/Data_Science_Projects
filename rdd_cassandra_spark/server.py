# creating a server
import socket
import time

host = 'localhost'
port = 9999
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((host, port))
serv.listen(5)

while True:
    print("Wating for connection")
    conn, addr = serv.accept()
    print("Connection successful")

    f = open("Data/data1.csv", "r")
    for x in f:
        print(x)

        conn.sendto(x.encode(), (host,port))
        time.sleep(0.001)
    conn.close()
    print('client disconnected')












