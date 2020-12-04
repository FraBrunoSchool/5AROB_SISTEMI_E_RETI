import socket as sck
import Config


def server():
    # get the hostname
    host = "192.168.178.33"
    port = 7000  # initiate port

    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)  # get instance

    s.bind((host, port))  # bind host address and port

    s.listen()  # number of client can listen simultaneously
    print("Sever in ascolto")
    conn, address = s.accept()  # accept new connection

    print(f"onnection from: {address}")
    ks = search_ks(conn, address)
    print(f"Chive privata comune {ks}")

    while True:
        data = conn.recv(1024).decode()  # receive data
        print(f"from connected user {address}:  {data}")
        if not data or data == "exit":
            # if data is not received or data is the word 'exit' to end the connection break
            print("Close the connection")
            break
        msg = input("->")
        conn.sendall(msg.encode())  # send data to the client

    conn.close()  # close the connection


def search_ks(conn, address):
    A = int(conn.recv(1024).decode())  # receive data
    print(f"from connected user {address}:  A = {A}")
    while True:
        b = int(input(f"Scegliere un numero 'b' minore di N : '{Config.KEY_PUBLIC_N}'"))
        if b < Config.KEY_PUBLIC_N: break
    print(f"b = {b}")
    conn.sendall(str(pow(Config.KEY_PUBLIC_g, b) % Config.KEY_PUBLIC_N).encode())
    ks = pow(A, b) % Config.KEY_PUBLIC_N
    print(f"Ks = {ks}")
    return ks


if __name__ == '__main__':
    server()
