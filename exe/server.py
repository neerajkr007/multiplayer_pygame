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

s.listen(3)
print("Waiting for a connection, Server Started")

players = [Player(150, 300, (0, 0, 0)), Player(850, 300, (255, 0, 0)), Player(500, 300, (255, 255, 255))]


def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply1 = ""
    reply2 = ""
    while True:
        try:
            data = pickle.loads((conn.recv(2048)))
            players[player] = data

            if not data:
                print("Disconnected.")
                break
            else:
                if player == 1:
                    reply1 = players[0]
                    reply2 = players[2]
                elif player == 2:
                    reply1 = players[1]
                    reply2 = players[0]
                else:
                    reply1 = players[1]
                    reply2 = players[2]

                print("Received: ", data)
                print("Sending : ", reply1)
                print("Sending : ", reply2)

            conn.sendall(pickle.dumps(reply1))
            conn.sendall(pickle.dumps(reply2))
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
