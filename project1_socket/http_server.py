# https://emalsha.wordpress.com/2016/11/22/how-create-http-server-using-python-socket/


import socket

HOST, PORT = '127.0.0.1', 1200

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.bind((HOST, PORT))
my_socket.listen(1)

while True:
    connection, address = my_socket.accept()
    req = connection.recv(1024).decode('utf-8')
    data = "HTTP/1.1 200 OK\r\n" \
           "Content-Type: text/html; charset=UTF-8\r\n\r\n" \
           "<html>Congratulations! You've downloaded the first Wireshark lab file!</html>\r\n"
    connection.send(data.encode())
    connection.close()
    print(req)

# while True:
#     connection, address = my_socket.accept()
#     data = "HTTP/1.1 200 OK\r\n" \
#            "Content-Type: text/html; charset=UTF-8\r\n\r\n" \
#            "<html>Congratulations! You've downloaded the first Wireshark lab file!</html>\r\n"
#     connection.send(data)
#     connection.close()
