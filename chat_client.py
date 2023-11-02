import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except ConnectionError as e:
            print(f"Erro na conexão: {e}")
            break
        except Exception as e:
            print(f"Erro: {e}")
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((HOST, PORT))
    except ConnectionRefusedError:
        print("Erro: Não foi possível conectar ao servidor. Verifique se o servidor está em execução.")
        return

    client_name = input("Digite seu nome: ")
    client.send(client_name.encode('utf-8'))

    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    while True:
        message = input()
        client.send(message.encode('utf-8'))

if __name__ == "__main__":
    main()
