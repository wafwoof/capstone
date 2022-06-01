import socket
import threading

HOST = '127.0.0.1'
PORT = 7777

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

# Define client / nickname lists
clients = []
nicknames = []


# BROADCAST
def broadcast(message):
    for client in clients:
        client.send(message)

# HANDLE
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            print(f"{nicknames[clients.index(client)]} says {message}")
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            break

# RECEIVE
def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}!")

        client.send("NICK".encode('utf-8'))
        nickname = client.recv(1024)

        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} connected to the server!\n".encode('utf-8'))
        client.send("Connected to the server".encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


# call method receive
print("       ######################\n\
       #  speakeasy server  #\n\
       #  written by wafw   #\n\
       # 2022-05-22 @ 17:41 #\n\
       #   version 0.1a     #\n\
       ######################\n")

print("AWAITING MESSAGES...")
receive()

