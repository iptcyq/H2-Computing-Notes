import socket

client = socket.socket()
client.connect(('127.0.0.1',5000))

print("This is a letter guessing game.")
guess = input("Enter guess (A-Z): ") + '\n'
client.sendall(guess.encode())
confirm = b''
while b'\n' not in confirm:
    confirm += client.recv(1024)

while confirm != b'yes\n':
    if confirm == b'bef\n':
        print("The answer is before your guess")
    else:
        print("The answer is after your guess")
    guess = input("Enter guess (A-Z): ") + '\n'
    client.sendall(guess.encode())

    confirm = b''
    while b'\n' not in confirm:
        confirm += client.recv(1024)

print("You win!")
client.close()
