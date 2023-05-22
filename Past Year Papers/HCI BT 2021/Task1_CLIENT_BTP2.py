# client
import socket
client = socket.socket()
client.connect(('127.0.0.1', 5000))

print("Guess a word of 5 distinct letters!\n")

def protocol():
    msg = b''
    while b'\n' not in msg:
        msg += client.recv(1024)
    return msg.decode()[:-1]

msg = protocol()
while msg == 'ok':
    guess = input("Guess a letter in the word:") + '\n'
    client.sendall(guess.encode())
    reply = protocol()
    print("YES\n") if reply=='Y' else print("NO\n")
    client.sendall(b'ok\n')
    msg = protocol()

word_guess = input("Guess the word:") + '\n'
client.sendall(word_guess.encode())
print()

reply = protocol()
if reply == 'win':
    print("You WIN!")
else:
    print(f"You LOSE! The correct word is {reply}")
client.sendall(b'ok\n')

client.close()
