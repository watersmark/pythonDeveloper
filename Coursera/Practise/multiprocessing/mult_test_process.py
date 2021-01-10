# для создания процессов используем модуль multiprocessing
# данный модуль работает на поддерживаемых операционных системах
# и находится в стандартной библиотеке python
# метод start() запускает процесс и аналогичен мектоду fork()
# метод join() завершает процесс и освобождает память
# можно наследоваться от класса Process и создавть свой класс
# в котором надо переопределить метод run и в методе init вызвать super

import multiprocessing
from multiprocessing import Process
import time


class PrintProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print("hello", self.name)


def name(name):
    print(f"Hello {name}")


if __name__ == "__main__":
    process = Process(target=name, args=("Bob", ))
    process.start()
    process.join()

    print("function process end")

    process = PrintProcess("Topa")
    process.start()
    process.join()

