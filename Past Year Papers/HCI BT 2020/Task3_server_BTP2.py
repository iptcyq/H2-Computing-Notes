import socket, random

server = socket.socket()
server.bind(('127.0.0.1', 5000))
server.listen()

client, addr = server.accept()
letter = chr(random.randint(65, 91)) #prob should comment that these are ord of A and Z

data = b''
while b'\n' not in data:
    data += client.recv(1024)
guess = data.decode()[0]
print(ord(guess), ord(letter))

while guess != letter:
    if ord(guess) < ord(letter): #technically no need ord()
        client.sendall(b'aft\n')
    else:
        client.sendall(b'bef\n')

    data = b''
    while b'\n' not in data:
        data += client.recv(1024)
    guess = data.decode()[0]   

client.sendall(b'yes\n')

client.close()
server.close()
