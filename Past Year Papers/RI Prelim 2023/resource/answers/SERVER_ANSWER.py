import socket
hello=False

def process_input(input_text):
    input_text = input_text.lower()
    global hello
    if "hello" in input_text:
        if "hello" in input_text and hello==False:
            hello=True
            return "Hi, how are you?"
        else:
            return "Hello again, welcome back!"
    elif "thanks" in input_text or "thank you" in input_text:
        return "You are most welcome."
    elif "i " in input_text.lower() and " you" in input_text.lower():
        parts = input_text.split()
        if parts.index('i') < parts.index('you'):
            indexA = parts.index('i')+1
            return f"You {parts[indexA]} me? I really {parts[indexA]} you too."
        else:
            return "Sorry, I do not understand..."
    else:
        return "Sorry, I do not understand..."

def main():
    server_socket = socket.socket()
    server_socket.bind(("127.0.0.1", 12345))
    server_socket.listen()
    print("Chatterbot server is listening.\n")
    while True:
        client_socket, client_address = server_socket.accept()
        while True:
            try:
                user_input = client_socket.recv(1024).decode()
                if not user_input:
                    break
                if user_input.lower() == "exit\n":
                    break
                print("Client:",user_input.strip())
                response = process_input(user_input)
                print("Chatterbot:",response)
                print('\n')
                client_socket.send(response.encode()+b'\n')
                
            except:
                print("Client disconnected.")
                break
        break

    print("Server is shutting down.")
    client_socket.close()
    server_socket.close()

main()
