# https://www.tutorialspoint.com/simple-chat-room-using-python


import socket
import select

IP = "127.0.0.1"
PORT = 7986
HEADER_LENGTH = 10

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((IP, PORT))

print("Server listening on: localhost on port: ", PORT)
name = input('Enter name: ')
server_socket.listen(1)


print("Waiting for incoming connections...")
conn, addr = server_socket.accept()



print("Received connection from: ", addr[0], "(",  addr[1], ")")
print("Connection by ('", addr[0], "', ", addr[1])

# print("Connection Established.  Connected From: {}, ({})".format(addr[0], addr[1]))

# get a connection from the client side
client_name = conn.recv(1024)
client_name = client_name.decode()
print(client_name + ' has connected.')
# print('Press /q to leave the chat room.')
conn.send(name.encode())

print("Waiting for message...")
print('Press /q to leave the chat room.')

#
# client = (conn.recv(1024)).decode()
# print(client + ' has connected.')

message = conn.recv(1024)
message = message.decode()
# print(s_name, ":", message)
print(client_name, '>', message)



while True:
    # conn, addr = server_socket.accept()
    # print("Waiting for message ...")
    # print("Received connection from ")
    # name = input(str("Enter your name: "))
    message = input('Me > ')

    if message == "/q":
        conn.send(message.encode())
        print("\n")
        # message = "Left chat room!"
        break

    conn.send(message.encode())

    client_message = conn.recv(1024)
    client_message = client_message.decode()

    print("client message: ", client_message)
    if client_message == '/q':
        conn.close()
        server_socket.close()
        print("\n")
        break

    # print(s_name, ":", message)
    print(client_name, '>', client_message)

