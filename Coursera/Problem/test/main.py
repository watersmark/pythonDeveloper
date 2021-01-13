from threading import Thread
import time
import threading

class Descriptor(object):

    def __init__(self, value):
        self.value = value

    def __get__(self, obj, obj_type):
        return self.value

    def __set__(self, obj, value):
        self.value = value * 5


class Iterator(object):
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == self.stop:
            raise StopIteration

        self.start += 1
        return self.start


class TempCreator(object):
    singleton = None
    var_desc = Descriptor(25)

    # __slots__ = ['tt', 'bb', 'age']

    def __init__(self, age):
        self.age = age

    # def __getattr__(self, item):
    #     return self.item

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

class StartThread(Thread):
    def __init__(self, value):
        super(StartThread, self).__init__()

    def run(self):
        with threading.RLock():
            for elem in range(5):
                print(elem)



if __name__ == "__main__":


    first = StartThread(10)
    second = StartThread(10)

    first.start()
    second.start()

    first.join()
    second.join()
