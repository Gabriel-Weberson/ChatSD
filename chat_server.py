import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

# Armazena as conexões dos clientes
clients = {}


def handle_client(client_socket, client_name):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break

            for name, sock in clients.items():
                if name != client_name:
                    sock.send(f"{client_name}: {message}".encode('utf-8'))
        except:
            break


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(2)  # Aceitar apenas duas conexões, para dois usuários

    print(f"Servidor de chat ouvindo em {HOST}:{PORT}")

    while len(clients) < 2:
        client, addr = server.accept()
        client_name = client.recv(1024).decode('utf-8')
        clients[client_name] = client

        print(f"Cliente {addr} conectado como {client_name}")

        for name, sock in clients.items():
            if name != client_name:
                sock.send(f"{client_name} entrou no chat.".encode('utf-8'))

        client_handler = threading.Thread(
            target=handle_client, args=(client, client_name))
        client_handler.start()


if __name__ == "__main__":
    main()
