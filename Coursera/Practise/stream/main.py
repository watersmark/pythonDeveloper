# рассмотрим концепцию потоков
# процесс делит адресное пространство
# в одном процессе могут быть несеольк потоков
# можно отнаследоваться от класса Thread
# и переопределить метод run и вызвать super в init


from threading import Thread

class PrintThread(Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(self.name)

def name(names):
    print(f"This is {names}")


th = Thread(target=name, args=(('Topa',)))
th.start()
th.join()

print('Первый поток отработал')

th = PrintThread('Mike')
th.start()
th.join()