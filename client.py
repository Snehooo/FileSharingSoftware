import socket
from tqdm import tqdm

size = 1024
s = socket.socket()
ip = input("Enter the Internet Protocol : ")

if ip == '':
    ip = 'localhost'
    print("Connecting in local machine!")

port = input("Enter the port number : ")

if port == '':
    port = 9999

s.connect((ip, int(port)))
print("Connected!")

filesize = s.recv(size).decode('utf-8')
filesize = str(filesize)
filename = input("Enter the file name : ")
bar = tqdm(range(int(filesize)), f"Receiving {filename}", unit='b', unit_scale=True, unit_divisor=size)

with open(filename, 'wb') as f:
    while True:
        data = s.recv(size)
        if not data:
            print('Received successfully!')
            break
        f.write(data)
        bar.update(len(data))
        
f.close()