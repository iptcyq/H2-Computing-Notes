# server
import socket, random
server = socket.socket()
server.bind(('127.0.0.1',5000))
server.listen()
client, addr = server.accept()

def protocol():
    msg = b''
    while b'\n' not in msg:
        msg += client.recv(1024)
    return msg.decode()[:-1]

f = open("Materials/Additional_Materials/WORDS.txt", 'r')
data = f.read().split("\n")
f.close()

word = data[random.randint(0,len(data)-1)]
guess = ""

for i in range(5):
    client.sendall(b'ok\n')
    guess = protocol()
    client.sendall(b'Y\n') if guess in word else client.sendall(b'N\n')
    continu = protocol()

client.sendall(b'next\n')
word_guess = protocol()
if word_guess == word:
    client.sendall(b'win\n')
else:
    word += '\n'
    client.sendall(word.encode())
continu = protocol()

client.close()
server.close()
