
# creating a server
import socket
import time
import pandas as pd
import csv

host = 'localhost'
port = 9999
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((host, port))
serv.listen(5)

while True:
    print("Wating for connection")
    conn, addr = serv.accept()
    print("Connection successful")

#    with open('Data/data1.csv', mode='r') as f:
#        reader = csv.reader(f, delimiter=",")
        #for row in reader:
        #    print(row)
    f = open("Data/data2.txt", "r", encoding="ISO-8859-1")

    for x in f:
        print(x)
        conn.sendto(x.encode(), (host,port))
        time.sleep(0.0000001)
    conn.close()
    print('client disconnected')












