# client
import socket
client = socket.socket()
client.connect(('127.0.0.1',5000))

print("Message Interpretation:")
print("G: correct digit at the correct position")
print("Y: correct digit at the wrong position")
print("R: wrong digit")
print()

def protocol():
    msg = b''
    while b'\n' not in msg:
        msg += client.recv(1024)
    return msg.decode()[:-1]

msg = protocol()
while msg == 'ok':
    guess = input("Enter guess (1000-9999):") + '\n'
    client.sendall(guess.encode())
    reply = protocol()
    if reply == "win" or reply == "lose":
        msg = reply
        break
    print(f"Your message is: {reply}")
    print()
    msg = protocol()

if msg == "win":
    print("You win the game!")
else:
    print("You lose the game!")
    client.sendall(b'ok\n')
    ans = protocol()
    print(f"Correct code is: {ans}")
    client.sendall(b'ok\n')

client.close()
