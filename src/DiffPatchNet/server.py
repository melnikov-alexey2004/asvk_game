import socket
import selectors
import sys
from typing import Literal
import logging

import cmd

# /etc/hosts
# /ets/services name port/protocol tcp or udp (check it, option -u  is udp)

# logging.LogRecord
#
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(levelname)-8s %(name)s: %(message)s',
#                     datefmt='%H:%M:%S')

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    datefmt='%H:%M:%S',
    fmt='%(asctime)s %(levelname)-8s %(name)s: %(message)s',
)
handler.setFormatter(formatter)

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)

root_logger.addHandler(handler)

sel = selectors.DefaultSelector()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
server.bind(('localhost', 1339))
server.listen()
sel.register(server, selectors.EVENT_READ)
logging.debug(f'Server start on port: {server.getsockname()[1]}')

def accept_conn():
    global server, sel

    client, addr = server.accept()
    # print(addr, client)
    sel.register(client, selectors.EVENT_READ | selectors.EVENT_WRITE)

    logging.debug(f'Client connected {addr}')

def handle_client(client: socket.socket, mask: int):
    if mask & selectors.EVENT_READ:
        data = client.recv(4096)
        if data:
            print([data])
            logging.debug(f'Get message from {client.getpeername()}')
        #     sel.unregister(client)
        #     client.close()
        else:
            # print([data])
            logging.debug(f'client {client.getpeername()} disconnected')
            # client disconnected
            sel.unregister(client)
            client.close()
            return

        data = data.decode()

        if mask & selectors.EVENT_WRITE:
            data  = data.encode()
            client.send(data)
            return
    # if mask & selectors.EVENT_WRITE:
    #     data = 'data response late... no echo message'
    #     client.send(data.encode())

while True:
    for sel_key, mask in sel.select(timeout=0.1):
        if sel_key.fileobj is server:
            accept_conn()
        else:
            # client
            handle_client(sel_key.fileobj, mask)

# server.close()