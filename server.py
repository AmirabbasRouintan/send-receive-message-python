import socket
import threading


HOST = '127.0.0.1'  # Standard loopback interface address
PORT = 3003        # Port to listen on


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)


clients = []
nicknames = []


def broadcast(message, sender_nickname):
    for client, nickname in zip(clients, nicknames):
        if nickname != sender_nickname:
            client.send(f"{sender_nickname}: {message}".encode())


def handle_client(client, nickname):
    while True:
        try:
            message = client.recv(1024).decode()
            if message:
                broadcast(message, nickname)

        except:
            index = clients.index(client)
            clients.remove(client)
            nickname = nicknames.pop(index)
            broadcast(f"{nickname} has left the chat.".encode(), "SERVER")
            client.close()
            break


def receive():
    while True:
        client, address = server_socket.accept()
        print(f"Connected with {str(address)}")
        clients.append(client)

        
        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} has joined the chat.".encode(), "SERVER")
        client.send("Connected to the server.".encode())


        thread = threading.Thread(target=handle_client, args=(client, nickname))
        thread.start()


print("Server is running...")
receive()
