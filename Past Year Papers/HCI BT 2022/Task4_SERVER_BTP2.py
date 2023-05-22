# server
import socket, random
server = socket.socket()
server.bind(('127.0.0.1',12345))
server.listen()
client, addr = server.accept()

def protocol():
    msg = b''
    while b'\n' not in msg:
        msg += client.recv(1024)
    return msg.decode()[:-1]

code = str(random.randint(1000,9999))
tries = 0
guess = '0000'
while tries <4 and guess != code:
    client.sendall(b'ok\n')
    guess = protocol()
    out = ""
    for i in range(4):
        if guess[i] == code[i]:
            out += "G"
        elif guess[i] in code:
            out += "Y"
        else:
            out += "R"
    out += '\n'
    client.sendall(out.encode())
    tries += 1

if tries < 4:
    client.sendall(b'win\n')
else:
    client.sendall(b'ok\n')
    guess = protocol()
    if guess == code:
        client.sendall(b'win\n')
    else:
        client.sendall(b'lose\n')
        continu = protocol()
        code += '\n'
        client.sendall(code.encode())
        continu = protocol()

client.close()
server.close()