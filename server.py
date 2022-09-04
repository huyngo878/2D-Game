import socket
from _thread import*
import sys

##server address
server = "192.168.0.3"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

##looking for connections/opens up port and allow how many people to connect
s.listen(3)
print("Waiting for user connection")

##split the cord in two int
def read_pos(str):
    str = str.split(",")
    return int(str[0], int(str[1]))
##make the int into (##, ##)
def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

pos = [(0, 0), (100, 100)]

def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = " "
    while True:
        ##recieve data from player if getting error increase size
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]
                print("Recieved: ", data)
                print("Sending: ", reply)
                conn.sendall(str.encode(make_pos(reply)))
        except:
            break
    
    print("Lost Connection")
    conn.close()

playerCount = 0

## start_new_thread runs the function threaded client so it runs all the time multiple times
## exmpl is multiple people playing the game this allow multiple functions to run
while True:
    conn, addr = s.accept()
    ##shows address of people who are connected
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, playerCount))
    playerCount += 1