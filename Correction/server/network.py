import socket


# Send a message to all clients
def sendTo(clients, str):
    for client in clients:
        if type(client) is socket.socket:
            client.send(str.encode())
