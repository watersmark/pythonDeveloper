from threading import Thread
from multiprocessing import Process

def print_name(name):
    print(name)
    print(f'name is {ord(str(name))}')


for elem in range(5):
    Thread(target=print_name, args=((elem,))).start()