import socket

client=socket.socket()
client.connect(("localhost", 9999))

print(client.recv(1024).decode())
name=input("Enter name:")
client.send(bytes(name,"utf-8"))
