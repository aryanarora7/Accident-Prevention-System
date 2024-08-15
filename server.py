import socket

# Define the server's IP address and port
SERVER_IP = '172.20.10.2'
SERVER_PORT = 12344

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP address and port
server_socket.bind((SERVER_IP, SERVER_PORT))

# Listen for incoming connections
server_socket.listen(1)
print("Server is listening for incoming connections...")

# Accept a client connection
client_socket, client_address = server_socket.accept()
print("Connected with client:", client_address)

try:
    while True:
        # Receive data from the client
        data = client_socket.recv(1024).decode()
        
        if not data:
            # No more data received, connection is closed
            break
        
        # Process the received data
        print("Received data:", data)
        
        # Simulate accident prevention logic
        if "stop" in data:
            print("Accident prevention system activated: Stop!")
        
except Exception as e:
    print("An error occurred:", str(e))

finally:
    # Close the client connection
    client_socket.close()
    
    # Close the server socket
    server_socket.close()
    print("Server socket closed.")
