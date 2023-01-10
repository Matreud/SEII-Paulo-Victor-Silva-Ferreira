# Importando bibliotecas
import socket
import threading
import time

# Definição de portas
PORT = 5050

# Tipo de codificação
FORMATO = "utf-8"

# Definição do IP
SERVER = "192.168.0.109"
ADDR = (SERVER, PORT)

# Conectando
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


#Divisor de pacotes
def handle_mensagens():
    while True:
        msg = client.recv(1024).decode()
        mensagem_splitada = msg.split("=")
        print(mensagem_splitada[1] + ": " + mensagem_splitada[2])


# Envio codificado
def enviar(mensagem):
    client.send(mensagem.encode(FORMATO))


# Envio de input
def enviar_mensagem():
    mensagem = input()
    enviar("msg=" + mensagem)

# Envio de nome
def enviar_nome():
    nome = input("Digite seu nome: ")
    enviar("nome=" + nome)


# Envio de mensagem
def iniciar_envio():
    enviar_nome()
    enviar_mensagem()


# Definição de threads
def iniciar():
    thread1 = threading.Thread(target=handle_mensagens)
    thread2 = threading.Thread(target=iniciar_envio)
    thread1.start()
    thread2.start()


iniciar()
