import socket
import threading

def handle_client(client_socket , address):
    while True:
        try:
            # Receive data from the client
            data = client_socket.recv(1024)
            if not data:
                # No data received, client has disconnected
                break

            # Process the received data
            # (you can replace this with your desired logic)
            print(f"Received data from client {address}: {data.decode()}")

            # Send a response back to the client
            response = "Message received"
            client_socket.send(response.encode())
        except:
            # An error occurred, client has disconnected
            break

    # Close the client socket
    client_socket.close()

def start_server():
   # IP4v , and protocol is TCP
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

    #name of your pc
    pc_name = socket.gethostname()

    #to get your local Ip
    ip = socket.gethostbyname(pc_name)
    # print(pc_name)
    print("your ip is :" + ip)
    
    #make a port
    s.bind((ip , 5000))

    s.listen()
    print("Server listening on {}:{}".format(ip,5000))

    while True:
        # Accept a client connection
        client_socket, client_address = s.accept()
        print("Accepted connection from {}:{}".format(*client_address))

        # Start a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket,client_address))
        client_thread.start()

# Start the server
start_server()