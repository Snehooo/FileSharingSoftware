import socket
from tqdm import tqdm
import os

# SENDER

size = 1024

server = socket.socket()
ip = input("Enter the Internet Protocol : ")

if ip == '':
    ip = 'localhost'
    print('Server in local machine!')
server.bind((ip, 9999))
print("Successfully created the server!")

server.listen(2)
filename = input("Enter the name of the file : ")
print("Waiting for the client to connect!")
client, adr = server.accept()
print("Client connected successfully!")

filesize = os.path.getsize(filename)
client.send(bytes(str(filesize), 'utf8'))

bar = tqdm(range(filesize), f"Sending {filename}", unit="b", unit_scale=True, unit_divisor=size)

with open(filename, 'rb') as f:
    while True:
        data = f.read(size)
        if not data:
            print('Sent successfully!')
            break

        client.send(data)
        bar.update(len(data))

f.close()