import socket

# Create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to an address and port
HOST = '127.0.0.1'  # Localhost
PORT = 56809
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(5)
print(f"Server is listening on {HOST}:{PORT}...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    # Receive data from the client
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Client says: {data}")

    # Send a response
    response = "Hello from server!"
    client_socket.send(response.encode('utf-8'))

    # Close the connection
    client_socket.close()
