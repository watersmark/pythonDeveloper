#  рассмотрим блокировку потоков
# потоки работают одновременно
# в методже join мы ждём оба потока
# команда threading.current_thread() позволяет узнать в каком мы сейчас находимся потоке
# команда threading.active_count() позволяет узнать сколько у нас потоков

import threading
import time


class Point(object):
    def __init__(self, x, y):
        self.mutex = threading.RLock()
        self.set(x, y)

    def get(self):
        with self.mutex:
            return (self.x, self.y)

    def set(self, x, y):
        with self.mutex:
            self.x = x
            self.y = y


def start(a, b):
    for elem in range(3):
        print(threading.current_thread())

        print(elem)
        time.sleep(5)

if __name__ == "__main__":

    th1 = threading.Thread(target=start, args=((10, 3)))
    th2 = threading.Thread(target=start, args=((10, 3)))

    print(threading.current_thread())

    th1.start()
    th2.start()

    print(threading.active_count())

    print(threading.current_thread())

    th1.join()
    th2.join()

    print("Both thread is end")

    my_point = Point(10, 20)
    my_point.set(15, 10)
    my_point.get()
