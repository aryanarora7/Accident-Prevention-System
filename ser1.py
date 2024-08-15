import socket

def calculate_additions(numbers):
    pn = sum(num for num in numbers if num > 0)
    nn = sum(num for num in numbers if num < 0)
    return pn, nn

def handle_client(client_socket):
    # Receive VIT-Register number from client
    register_number = client_socket.recv(1024).decode()
    print(f"Received VIT-Register number: {register_number}")

    # Receive 'n' integers from client
    n = int(client_socket.recv(1024).decode())
    print(f"Received {n} integers:")

    numbers = []
    for _ in range(n):
        number = int(client_socket.recv(1024).decode())
        numbers.append(number)
        print(number)

    # Compute additions
    pn, nn = calculate_additions(numbers)
    print(f"PN: {pn}")
    print(f"NN: {nn}")

    # Send PN, NN to client
    client_socket.send(str(pn).encode())
    client_socket.send(str(nn).encode())

    client_socket.close()

def start_server():
    host = 'localhost'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Server started.")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Client connected: {addr[0]}:{addr[1]}")

        handle_client(client_socket)

if __name__ == '__main__':
    start_server()
