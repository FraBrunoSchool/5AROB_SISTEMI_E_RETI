import socket as sck
import Config


def client():
    # get the server name
    host = "192.168.178.33"
    port = 7000  # server port number

    print("creo istanza")

    c = sck.socket(sck.AF_INET, sck.SOCK_STREAM)  # instantiate
    c.connect((host, port))
    print("connect")
    print("Enter 'exit' to end the connection")

    ks = search_ks(c)
    print(f"Chive privata comune {ks}")
    msg = input("->")

    while True:
        c.sendall(msg.encode())  # send message
        data = c.recv(1024).decode()  # receive response
        print(f"Received from server: {data}")  # show response
        msg = input("->")  # again take input
        if msg == "exit":
            c.sendall(msg.encode())  # send message
            print("Close the connection")
            break
    c.close()  # close the connection


def search_ks(c):
    while True:
        a = int(input(f"Scegliere un numero 'a' minore di N : '{Config.KEY_PUBLIC_N}'"))
        if a < Config.KEY_PUBLIC_N: break
    print(f"a = {a}")
    c.sendall(str(pow(Config.KEY_PUBLIC_g, a) % Config.KEY_PUBLIC_N).encode())  # send message
    B = int(c.recv(1024).decode())  # receive response
    print(f"Received from server: B = {B}")  # show response
    ks = pow(B, a) % Config.KEY_PUBLIC_N
    print(f"Ks = {ks}")
    return ks


if __name__ == '__main__':
    client()
