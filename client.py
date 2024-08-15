import socket

# Define the server's IP address and port
SERVER_IP = '172.20.10.3'
SERVER_PORT = 12344

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((SERVER_IP, SERVER_PORT))
print("Connected to server:", SERVER_IP)

try:
    while True:
        # Get data from the user
        data = input("Enter data to send: ")
        
        if not data:
            # No data entered, end the connection
            break
        
        # Send the data to the server
        client_socket.sendall(data.encode())
        print("Data sent.")
        
except Exception as e:
    print("An error occurred:", str(e))

finally:
    # Close the client socket
    client_socket.close()
    print("Client socket closed.")
