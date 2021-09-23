from hashlib import sha256
from os import urandom
from threading import Thread

TARGET = '20020923'
TARGET_LENGTH = len(TARGET)
THREAD_NUMBER = 64

basket = None
stop = False

def mine():
    global stop, basket
    threads = []
    for _ in range(THREAD_NUMBER):
        threads.append(Thread(target=mine_worker))
    for t in threads:
        print('Thread started.')
        t.start()
    while basket == None:
        continue
    stop = True
    return basket

def mine_worker():
    global TARGET, TARGET_LENGTH, basket, stop
    nonce = urandom(8)
    while not stop and sha256(nonce).hexdigest()[-TARGET_LENGTH:] != TARGET:
        nonce = urandom(8)

    
    basket = nonce


with open('hbd.bin', 'wb') as fw:
    fw.write(mine())
