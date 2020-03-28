import socket
s=socket.socket()
print("Socket created..")
s.bind(("localhost", 9999))
s.listen(5)
print("waiting for connnections..")

while True:
    conn,addr=s.accept()
    print("connected with:",addr)
    conn.send(bytes("WELCOME ","utf-8"))
    name=conn.recv(1024).decode()
    print("connected person:",name)