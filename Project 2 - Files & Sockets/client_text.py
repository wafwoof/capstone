import socket
import threading
import tkinter
import tkinter.scrolledtext
from tkinter import simpledialog


# Check if process is main
checkIfMain = lambda x: True if __name__ == "__main__" else False
if checkIfMain == False:
    exit()


HOST = '127.0.0.1'
PORT = 7777

class Client:

    def __init__(self, host, port):


        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

        # Select username
        self.nickname = input("Please choose a nickname: ")


        text_thread = threading.Thread(target=self.write)
        receive_thread = threading.Thread(target=self.receive)

        # 2022-05-22@9:41pm --- maybe try switching the order of these:
        text_thread.start()
        receive_thread.start()


    def write(self):
        while True:
            
            message = input()
            message = f"{self.nickname}: {message}"
            self.sock.send(message.encode('utf-8'))
            self.sock.send("\n".encode('utf-8'))

    def stop(self):
        self.running = False
        self.sock.close()
        exit(0)


    def receive(self):
        while True:
            try:
                message = self.sock.recv(1024).decode('utf-8')
                if message == 'NICK':
                    self.sock.send(self.nickname.encode('utf-8'))
                else:
                    print(message)
            except ConnectionAbortedError:
                break
            except:
                print("THERE HAS BEEN AN ERROR")
                self.sock.close()
                break


client = Client(HOST, PORT)
    
