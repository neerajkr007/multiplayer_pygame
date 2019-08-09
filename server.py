import socket
from _thread import *
from player import Player
import pickle

server = "25.81.81.215"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

players = [Player(150, 300, (0, 0, 0)), Player(850, 300, (255, 0, 0))]#, Player(500, 300, (255, 255, 255))]


def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    #reply2 = ""
    while True:
        try:
            data = pickle.loads((conn.recv(2048)))
            players[player] = data

            if not data:
                print("Disconnected.")
                break
            else:
                if player == 1:
                    reply = players[0]
                #elif player == 2:
                 #   reply = players[1]
                else:
                    reply = players[1]

                print("Received: ", data)
                print("Sending : ", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()


currentPlayer = 0

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
