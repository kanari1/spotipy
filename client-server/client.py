import time, socket, sys

IP = "127.0.0.1"
PORT = 7986

print("\nWelcome to Chat Room\n")
print("Initializing...\n")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
name = input(str("Enter your name: "))
server_socket.connect((IP, PORT))
print("Connected to: localhost on port: ", PORT)
print("Type /q to quit")

server_socket.send(name.encode())
s_name = server_socket.recv(1024)
s_name = s_name.decode()
print(s_name, "has joined the chat room.")


while True:

    message = input(str("Enter message to send: "))
    if message == "/q":
        # message = "Left chat room!"
        server_socket.send(message.encode())
        server_socket.close()
        print("\n")
        break
    server_socket.send(message.encode())

    rcv_message = server_socket.recv(1024)
    rcv_message = rcv_message.decode()

    if rcv_message == '/q':
        server_socket.close()
        print("\n")
        break

    print("Message: ", rcv_message)