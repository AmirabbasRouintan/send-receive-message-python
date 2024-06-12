import socket
import threading

nickname = input("Choose a nickname: ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 3003))

def receive():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message == "NICKNAME":
                client_socket.send(nickname.encode())
            else:
                print(message)
        except:
            print("An error occurred!")
            client_socket.close()
            break

def write():
    while True:
        message = input('')
        client_socket.send(message.encode())

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()